---
name: renders
description: Turn a room photo into pictures of the same room with new finishes. Keeps walls, doors and camera, changes only the finish list. Sends the photo to Google's and OpenAI's image models with the user's own keys, only after they say yes. Use for render this photo, before and after, show this room with new doors, carpet, lights or paint.
---

# renders

A room photo goes in. Two pictures of the same room with new finishes come back, side by side. Claude runs it. Google's and OpenAI's image models draw the pictures.

## Install, once

1. You need Claude Code, the version of Claude that runs on your computer.
2. Put this folder in your Claude skills folder as `renders`. On a Mac that is `~/.claude/skills/renders`. Or ask Claude Code: "Install the renders skill from github.com/bernan-ai/ai-dropins, folder renders/skill."
3. Get one or both keys. Gemini: aistudio.google.com/apikey. OpenAI: platform.openai.com/api-keys. Image models usually need billing turned on. OpenAI may ask you to verify your organization first.
4. Save each key yourself, in your own terminal, never in the chat. On a Mac:
   `echo 'export GEMINI_API_KEY=paste-your-key' >> ~/.zshrc`
   `echo 'export OPENAI_API_KEY=paste-your-key' >> ~/.zshrc`
   On Windows: `setx GEMINI_API_KEY paste-your-key` and `setx OPENAI_API_KEY paste-your-key`.
5. Open a new terminal window and start Claude Code again.

One key is enough. Two keys give you two pictures to pick from.

## Use

Type **render this photo** and drop in the photo, straight from your phone.

## Undo

- Your photo never changes. Pictures land in a new folder beside it.
- Delete this folder to remove the skill.
- Delete the export lines from `~/.zshrc` to remove the keys, or run `setx GEMINI_API_KEY ""` on Windows.

## For Claude

Run these steps as a short conversation. Plain words, short messages.

1. **Photo.** Ask for the raw photo from their phone. Never rotate, crop or convert it yourself; the script handles rotation, HEIC and hidden data.
2. **Finish list.** Look at the photo. In one message, ask what they want for each thing that could change: doors, door hardware, trim, elevator doors, floor or carpet, light fixtures, wall paint, base molding. "You decide" means a clean, neutral choice. Write one list, one item per change.
3. **Preview.** Run `python3 make_render.py --photo "<photo>" --list "<item>, <item>"` from this skill's folder. Without `--yes` it sends nothing. Show them the list and the cost line. Ask: "Make them?"
4. **Make.** On a yes, run the same command with `--yes`. One key set means one picture. No key at all: give them the prompt the preview printed and tell them to paste it into ChatGPT or Gemini with the same photo.
5. **Show.** Open the before and after pictures side by side. Check that doors, frames and ceiling lines sit in the same spots. Check each list item really changed. Name any miss in one line.
6. **Fix.** For a miss, offer one rerun with the missed item said more plainly. Never rerun without a yes.

Rules:

- Never send the photo anywhere but the two image models, and only after a yes.
- Never ask for a key in the chat, and never write a key into any file.
- Never overwrite or delete their files.
- Never say a picture exists unless the script printed "saved."
- A picture is a design idea. Never present it as a measured drawing or a price.
