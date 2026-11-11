#!/usr/bin/env python3
"""Turn one room photo into after pictures that keep the room and change only your finish list.

Usage:
  python3 make_render.py --photo hallway.jpg --list "navy doors, white trim, gray carpet tile"
  python3 make_render.py --photo hallway.jpg --list finishes.txt --engine gemini --yes

Keys come from your environment only: GEMINI_API_KEY and OPENAI_API_KEY.
Without --yes it prints the plan, the prompt and the cost, and sends nothing.
It writes new files in a new folder beside your photo. It never changes your photo.
"""
# cli-only-exempt: image models have no command-line route; the reader runs this with their own key.
import argparse, base64, datetime, json, os, shutil, subprocess, sys, tempfile, urllib.error, urllib.request, uuid

GEMINI_MODEL = "gemini-3-pro-image"
OPENAI_MODEL = "gpt-image-2"
GEMINI_BASE = "https://generativelanguage.googleapis.com"
OPENAI_BASE = "https://api.openai.com"
COST = {"gemini": 0.15, "openai": 0.08}   # rough US dollars per picture, November 2026

GEOMETRY_LOCK = (
    "CRITICAL CONSTRAINT: this is a photograph of a real existing space. Preserve the EXACT "
    "geometry, camera position, lens and perspective, vanishing point, proportions, wall and "
    "ceiling positions, door and window positions and sizes, and the overall architecture of "
    "the source photo with zero deviation. The result must look like the SAME real space "
    "photographed again after renovation, never a different or re-imagined room. Do not move, "
    "add, remove, resize, or restyle anything that is not explicitly listed below."
)
KEEP_REST = (
    "Everything else in the photo remains exactly as it is, including layout and fixtures not "
    "listed. Photoreal with correct lighting, shadows and reflections, professional real-estate "
    "listing quality. No text, labels, watermarks, or people."
)
# OpenAI's editor treats "change only X" as "keep it all" and barely edits. Saying it is a
# finished renovation makes it commit. Gemini follows the plain change list.
COMMIT = ("Re-render this photo as the finished, professionally photographed version of THE SAME "
          "space. Commit fully to the new finishes: this is a renovation, not a touch-up.")


def build_prompt(changes, engine):
    lines = ["Photorealistic interior renovation render."]
    if engine == "openai":
        lines.append(COMMIT)
    lines += [GEOMETRY_LOCK, "", "Change ONLY these elements:"]
    lines += [f"  - {c}" for c in changes]
    lines += ["", KEEP_REST]
    return "\n".join(lines)


def read_list(text):
    if os.path.isfile(text):
        text = open(text, encoding="utf-8").read()
    items = [p.strip(" -*\t") for line in text.splitlines() for p in line.split(",")]
    return [i for i in items if i]


def prep_photo(photo, workdir):
    """Bake the phone's rotation into the pixels, strip location and camera data, cap at 2048 px.
    Feed the raw phone photo: never rotate it yourself first."""
    src = photo
    if photo.lower().endswith((".heic", ".heif")):
        if not shutil.which("sips"):
            raise SystemExit("HEIC photo: on a Mac this converts itself. Elsewhere, save it as JPG first.")
        src = os.path.join(workdir, "converted.jpg")
        subprocess.run(["sips", "-s", "format", "jpeg", photo, "--out", src],
                       capture_output=True, check=True)
    try:
        from PIL import Image, ImageOps
    except ImportError:
        print("note: Pillow is not installed, so the photo goes as is, with its hidden data.\n"
              "      To strip it and lock the rotation: python3 -m pip install --user pillow")
        return src
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    im.thumbnail((2048, 2048))
    clean = Image.new("RGB", im.size)
    clean.paste(im)
    out = os.path.join(workdir, "before.png")
    clean.save(out)
    return out


def image_size(path):
    try:
        from PIL import Image
        return Image.open(path).size
    except Exception:
        return (0, 0)


def gemini_aspect(w, h):
    ratios = {"1:1": 1.0, "2:3": 2 / 3, "3:2": 1.5, "3:4": 0.75, "4:3": 4 / 3,
              "4:5": 0.8, "5:4": 1.25, "9:16": 0.5625, "16:9": 16 / 9}
    return min(ratios, key=lambda k: abs(ratios[k] - (w / h))) if w and h else None


def post(url, body, headers):
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        try:
            return json.loads(e.read())
        except Exception:
            return {"error": {"message": f"HTTP {e.code}"}}
    except (urllib.error.URLError, TimeoutError, ValueError) as e:
        return {"error": {"message": str(e)}}


def call_gemini(photo, prompt, key):
    data = base64.b64encode(open(photo, "rb").read()).decode()
    mime = "image/png" if photo.endswith(".png") else "image/jpeg"
    cfg = {"responseModalities": ["IMAGE"], "imageConfig": {"imageSize": "2K"}}
    aspect = gemini_aspect(*image_size(photo))
    if aspect:   # an unmatched frame makes the model re-crop the room
        cfg["imageConfig"]["aspectRatio"] = aspect
    body = {"contents": [{"parts": [{"text": prompt},
                                    {"inline_data": {"mime_type": mime, "data": data}}]}],
            "generationConfig": cfg}
    d = post(f"{GEMINI_BASE}/v1beta/models/{GEMINI_MODEL}:generateContent",
             json.dumps(body).encode(), {"x-goog-api-key": key, "Content-Type": "application/json"})
    if "error" in d:
        return None, d["error"].get("message", "error")
    for p in (d.get("candidates") or [{}])[0].get("content", {}).get("parts", []):
        blob = (p.get("inlineData") or p.get("inline_data") or {}).get("data")
        if blob:
            return base64.b64decode(blob), "ok"
    return None, "no picture in the answer"


def call_openai(photo, prompt, key):
    w, h = image_size(photo)
    size = "1024x1536" if h >= w * 1.2 else "1536x1024" if w >= h * 1.2 else "1024x1024"
    boundary = uuid.uuid4().hex
    fields = {"model": OPENAI_MODEL, "prompt": prompt, "size": size, "quality": "medium"}
    body = b""
    for k, v in fields.items():
        body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n").encode()
    mime = "image/png" if photo.endswith(".png") else "image/jpeg"
    body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"image\"; "
             f"filename=\"{os.path.basename(photo)}\"\r\nContent-Type: {mime}\r\n\r\n").encode()
    body += open(photo, "rb").read() + f"\r\n--{boundary}--\r\n".encode()
    d = post(f"{OPENAI_BASE}/v1/images/edits", body,
             {"Authorization": f"Bearer {key}", "Content-Type": f"multipart/form-data; boundary={boundary}"})
    if "error" in d:
        return None, d["error"].get("message", "error")
    try:
        return base64.b64decode(d["data"][0]["b64_json"]), "ok"
    except Exception:
        return None, "no picture in the answer"


def main():
    ap = argparse.ArgumentParser(description="photo in, same room with new finishes out")
    ap.add_argument("--photo", required=True)
    ap.add_argument("--list", required=True, help="the finish list, comma separated, or a text file")
    ap.add_argument("--engine", choices=["both", "gemini", "openai"], default="both")
    ap.add_argument("--yes", action="store_true", help="really send and spend; without it, a preview")
    a = ap.parse_args()

    photo = os.path.expanduser(a.photo)
    if not os.path.isfile(photo):
        raise SystemExit(f"photo not found: {photo}")
    changes = read_list(a.list)
    if not changes:
        raise SystemExit("the finish list is empty")
    engines = ["gemini", "openai"] if a.engine == "both" else [a.engine]
    keys = {"gemini": os.environ.get("GEMINI_API_KEY"), "openai": os.environ.get("OPENAI_API_KEY")}
    ready = [e for e in engines if keys[e]]
    for e in engines:
        if not keys[e]:
            print(f"skip {e}: no {e.upper()}_API_KEY set")

    cost = sum(COST[e] for e in ready)
    print(f"plan: {len(ready)} picture(s), about ${cost:.2f} on your own key")
    for e in engines:
        print(f"\nprompt for {e}:\n{build_prompt(changes, e)}")
    if not a.yes or not ready:
        print("\npreview only: nothing sent. Add --yes to make the pictures.")
        return

    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    out = os.path.join(os.path.dirname(os.path.abspath(photo)), f"renders-{stamp}")
    os.makedirs(out)
    with tempfile.TemporaryDirectory() as work:
        sent = prep_photo(photo, work)
        shutil.copy(sent, os.path.join(out, "before" + os.path.splitext(sent)[1]))
        for e in ready:
            call = call_gemini if e == "gemini" else call_openai
            img, msg = call(sent, build_prompt(changes, e), keys[e])
            if not img:
                print(f"{e}: failed: {msg}")
                continue
            path = os.path.join(out, f"after-{e}.png")
            open(path, "wb").write(img)
            bw, bh = image_size(sent)
            aw, ah = image_size(path)
            if bw and aw and (bw > bh) != (aw > ah):
                print(f"{e}: came back sideways. Run it again with the raw phone photo.")
            print(f"{e}: saved {path}")
    print(f"\nfolder: {out}")


if __name__ == "__main__":
    sys.exit(main())
