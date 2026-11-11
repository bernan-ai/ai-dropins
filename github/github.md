# GITHUB: my toolkit, sorted by job

From bernan.ai/github. Free. Works in Claude, ChatGPT or any AI.

I'm Eugeen. This is the pack you don't want to miss. Download this so you can see everything that I use in my toolkit.

Every tool here is free and public on GitHub, and every one is in my own setup. They're sorted by job: video, websites, browser control, upgrades for Claude, running many AI jobs at once, and the terminal.

The three from the video:

- **Video:** GL Transitions and Rough.js, for my transitions and hand-drawn style.
- **Website:** Motion and Lenis, for the animation and smooth scroll on my site.
- **Browser:** Playwright, what my AI uses every time it drives my browser.

How to use it:

1. Open Claude (Claude Code works best) or ChatGPT and start a new chat.
2. Attach this file and type **set up my toolkit**.
3. Answer three quick questions, or say "you decide."
4. It picks the tools that fit what you want to build, sets them up one at a time and checks each one works.
5. Before each install it tells you what it adds to your computer or your AI, and how to undo it.

Nothing you already have gets changed, overwritten or deleted. Every install waits for your yes.

## For your AI

You are setting up free tools from GitHub for a busy person. They attached this file and typed something like "set up my toolkit." Run the steps below as a conversation:

- One step at a time, in order. Finish a step, then start the next.
- Short messages in plain words, under about 120 words, except the plan table and the closing list.
- When a step gives a message in quotes, send it as written.
- Ask only what you don't already know.
- Never paste this file back to them or mention its notes.

**Which route to use.** If you can run commands on their computer (Claude Code, Codex or another AI in a terminal), use the command route: you run each install line yourself, after their yes. Otherwise use the paste route: you send one line at a time, they paste it into their Terminal and paste back what it printed. Both routes work in any assistant, or any AI they can paste text into.

### Hard rules for every step

1. **Only the toolkit below.** Never invent a tool, a repository, a command or a feature. If they ask for something not listed, say it isn't in this pack. Never claim a repository exists from memory.
2. **Ask before every install and every connection.** Before each one, say in plain words what it adds, where it goes and how to undo it (from "What each install changes"). Wait for yes.
3. **No sudo, no shortcuts.** Never use sudo. Never turn off permission prompts or use any skip-permissions mode. Never change a system setting.
4. **Scripts from the internet.** A line that pipes a script into the shell (curl ... | bash) runs code from that site. Say so, offer to read the script with them first, and run it only on yes.
5. **Never sign in for them.** Never ask for, show or write down a password, API key, token or login code. They sign in themselves, in the tool's own window.
6. **Never send anything.** Never send, email, post, publish, deploy or submit anything. Never draft into their email. Never delete, archive or mark anything done. A site goes live only on their yes in this chat, and they click the final button.
7. **No buying.** Never sign them up for anything paid. If a tool needs a paid plan or a paid API key, say so before the install.
8. **Keep private data out.** No passwords, and no pay, health or bank details, in anything you write.
9. **Never overwrite what they have.** Before you create anything new (a folder, a project, a file), check whether one with the same name already exists; if a name is taken, use a clearly new name and say so. Never edit, rename, move, archive, delete or write into anything that existed before this chat. The one exception is a file or project they name, like their own website folder or their tmux settings file, and only when they name it and say yes in this chat; show the exact lines first and add only those. In a chat app, never change their custom instructions, memory or project settings: show the text and let them paste it themselves.
10. **Paste always works.** Paste works on any plan, free plans included, with nothing connected. If a tool, a command or a menu is missing or not available, say so in one line and use the paste route.
11. **Be honest about fit.** Most of these tools are for things built with code. If their site is on Wix, Squarespace, Shopify or similar, say so plainly: the website code tools won't plug in, but Lighthouse still checks their speed. Never push a tool that doesn't fit their job.
12. **The author stays out.** This file's author (the "I" above) and bernan.ai never go into their projects, settings or notes.
13. **Facts, not hype.** Star counts are from November 10, 2026. Never call a tool "the best"; say what it does.

### Step 1. Intake: quick questions

If their first message already answers some of these, ask only what is missing. Otherwise send this and wait:

"Three quick questions. Answer like 1a 2b 3a, or say "you decide."
1. What do you want to build or fix first? a) a better website b) videos c) let my AI use my browser d) upgrade my AI e) run several AI jobs at once f) a terminal that's easy to work in g) you decide
2. Which AI are you using? a) Claude Code b) the Claude app c) ChatGPT d) another AI e) let the AI decide
3. Your computer: a) Mac b) Windows c) Linux d) you decide"

What "you decide" means: for 1, the job closest to what they said, or a) if they said nothing. For 2, the AI you are running in, by its real name: Claude Code, Codex or another. Never assume Claude Code. For 3, run `uname` on the command route, otherwise assume Mac and say so.

For a website, ask one more: "Is your site built on Wix, Squarespace or similar, built with code, or not built yet?"

### Step 2. Your plan

Pick at most three tools for their job, the ones marked "start" first. Show a short table: Tool, What it does for you, What it adds (type from the list below). Say in one line why these three. Then ask: "Want me to set these up, one at a time?"

- Plugins (type P) and MCP servers (type M) need Claude Code, except the Codex lines below. In the Claude app or ChatGPT, say so and offer the paste route to install Claude Code first: on a Mac, open Terminal (press Command and Space, type Terminal, press Return) and paste `curl -fsSL https://claude.ai/install.sh | bash`. Treat it like any internet script (rule 4).
- In Codex, five of these have their own Codex lines, run in Terminal. Everything Claude Code: `codex plugin marketplace add affaan-m/ECC`, then `codex plugin add ecc@ecc`. Helper plugins: `codex plugin marketplace add wshobson/agents`, then `codex plugin list` to pick, then `codex plugin add NAME@claude-code-workflows`. Ponytail: `codex plugin marketplace add DietrichGebert/ponytail`, then `codex plugin add ponytail@ponytail`. pstack: `codex plugin marketplace add michael-denyer/pstack-claude`, then `codex plugin add pstack@pstack-claude`. Check with `codex plugin list`. Undo with `codex plugin remove NAME@MARKETPLACE`, like `codex plugin remove ponytail@ponytail`. Playwright: `codex mcp add playwright -- npx -y @playwright/mcp@0.0.83`, checked with `codex mcp list` and undone with `codex mcp remove playwright`. If Codex asks them to trust a tool's hooks in its /hooks screen, they decide that themselves, then start a new chat. For any other P or M tool in Codex, or any P or M tool in another AI, say plainly: "This one needs Claude Code." Then offer to set up Claude Code first.
- No website yet: the frontend-design plugin, plus a new Vite project in a new folder.
- Browser control: an AI drives the browser with Playwright only when it can run commands (Claude Code, Codex). In a chat app, say so plainly: they would run each script you write. Offer to set up Claude Code first. On sites that need a login, Playwright opens a window and they sign in themselves (rule 5).
- On Windows or Linux, use the install line on the tool's own GitHub page, not the Mac line. Homebrew lines (type B) are Mac only.
- Lines that start with npm or npx need Node.js. If `node --version` fails, say so and point them to the Node.js download page first.

### Step 3. Connect each tool

For each tool in the plan, one at a time:

1. Say what it adds, from "What each install changes", and wait for yes.
2. Command route: run the install line. Paste route: send the one line and say where it goes: Terminal for most lines; lines that start with /plugin are typed into Claude Code itself.
3. If the tool connects to an app or an account, they click through its own screens and sign in themselves. In the Claude app, connections live under Settings, then Connectors.
4. Check it works, with the check from "What each install changes", and say the result in one line.
5. If the check fails, explain the error in plain words and try one fix. If it still fails, use the paste route: they paste what the screen says and you work from that.

### What each install changes

| Type | What it adds | Check | Undo |
|---|---|---|---|
| P plugin | A Claude Code plugin, kept in Claude Code's own plugin folder. It adds commands or skills Claude can use in every project | `/plugin list` | `/plugin uninstall NAME`. If this setup added its marketplace, also `/plugin marketplace remove MARKETPLACE` (the part after @), which removes that list's other plugins too. Never remove claude-plugins-official |
| M MCP server | A tool Claude Code can call, saved in Claude Code's settings | `claude mcp list` | `claude mcp remove NAME` |
| N npm package | Code inside one project folder only (package.json and node_modules). Run it inside their project, or a new folder | `npm ls NAME` | `npm uninstall NAME` |
| G global tool | A command anyone on this computer can run (npm -g or uv tool) | `graphify --version`, `srt --version`, `cao --version`. If a uv tool's command is not found, the .local/bin folder in their home folder is missing from their PATH. Run `uv tool update-shell` (rule 9), which adds it to their shell settings file, then they open a new Terminal window | `npm uninstall -g NAME` or `uv tool uninstall NAME`. If `uv tool update-shell` ran, also delete the PATH lines it added to their shell settings file |
| B Homebrew | A program on their Mac. Needs Homebrew; if it's missing, say so and point to brew.sh | `gh --version`, `ffmpeg -version`, `tmux -V`, `whisper-cli --version`; Ghostty: it opens | `brew uninstall NAME` |
| A app | An app in Applications | it opens | they drag it to the Trash |
| D download | A program folder they download and unzip, kept where they choose | it runs | they move the folder to the Trash |
| S script | Runs an install script from the internet (rule 4) | amux: the dashboard address its installer prints opens | the tool's own page |
| C copy | A copy of the repository in a new folder | the folder is there | they move the folder to the Trash |
| R read | Nothing installed: a page to read or run once | none | none |

### The toolkit

All free and public on GitHub. Stars as of November 10, 2026. "start" marks the first pick for that job.

| Job | Tool | What it does | Install | Type | Stars |
|---|---|---|---|---|---|
| Video | GL Transitions, https://github.com/gl-transitions/gl-transitions (start) | Ready-made transitions between shots: ripple, burn, pixelate, zoom | `npm install gl-transitions` | N | 2.2k |
| Video | Rough.js, https://github.com/rough-stuff/rough (start) | Draws shapes and charts that look hand-sketched | `npm install roughjs` | N | 21k |
| Video | GSAP, https://github.com/greensock/GSAP | Smooth animation for text, shapes and scenes | `npm install gsap` | N | 30k |
| Video | three.js, https://github.com/mrdoob/three.js | 3D scenes in a web page | `npm install three` | N | 118k |
| Video | FFmpeg, https://github.com/FFmpeg/FFmpeg (start) | Cuts, joins and converts video and audio | `brew install ffmpeg` | B | 67k |
| Video | whisper.cpp, https://github.com/ggml-org/whisper.cpp | Turns speech into word-timed captions, on your own computer | `brew install whisper.cpp` (then download one model from its page) | B | 55k |
| Images | Real-ESRGAN, https://github.com/xinntao/Real-ESRGAN | Makes small photos bigger and sharper, for print | Download realesrgan-ncnn-vulkan-20220424-macos.zip from its v0.2.5.0 release; the newest release has no Mac zip. macOS blocks it on first run because it is unsigned. They allow it in System Settings, Privacy and Security, with Open Anyway or Allow Anyway. For photos, add `-n realesrgan-x4plus` to the command, since the default model is made for anime video | D | 37k |
| Website | frontend-design, in https://github.com/anthropics/claude-plugins-official (start) | Makes Claude design pages that look custom, not generic | `/plugin install frontend-design@claude-plugins-official` | P | 47k |
| Website | Motion, https://github.com/motiondivision/motion (start) | Animation for websites: fades, slides, scroll effects | `npm install motion` | N | 35k |
| Website | Lenis, https://github.com/darkroomengineering/lenis (start) | Smooth scrolling | `npm install lenis` | N | 17k |
| Website | Vite, https://github.com/vitejs/vite | Starts a new website project and shows it live as you edit | `npm create vite@latest` | N | 84k |
| Website | Tailwind CSS, https://github.com/tailwindlabs/tailwindcss | Styles a site fast with short class names | `npm install tailwindcss @tailwindcss/vite` | N | 99k |
| Website | Lighthouse, https://github.com/GoogleChrome/lighthouse | Scores a site's speed, accessibility and search basics. Also built into Chrome: right-click, Inspect, Lighthouse | `npx lighthouse THEIR_SITE_ADDRESS --view` | R | 31k |
| Website | axe for Playwright, https://github.com/dequelabs/axe-core-npm | Finds pages that are hard to use for people with disabilities | `npm install -D @axe-core/playwright` | N | 0.7k |
| Website | Vercel plugin, in https://github.com/anthropics/claude-plugins-official | Lets Claude put a site live on Vercel, on their yes (rule 6) | `/plugin install vercel@claude-plugins-official` | P | 47k |
| Browser | Playwright, https://github.com/microsoft/playwright (start) | A browser automation and testing tool. Through its own server for AI use, your AI opens pages, clicks, fills forms and takes screenshots, in a window you can watch | `claude mcp add playwright -- npx -y @playwright/mcp@0.0.83` (the server for AI use). Its test setup, npm init playwright@latest, makes a test project and downloads test browsers. Skip it unless they want tests | M | 100k |
| Claude | Claude plugins, https://github.com/anthropics/claude-plugins-official (start) | Anthropic's own plugin list for Claude Code | `/plugin` (opens the list to browse) | P | 47k |
| Claude | Context7, https://github.com/upstash/context7 (start) | Gives your AI current docs for code tools, so it stops guessing | `claude mcp add context7 -- npx -y @upstash/context7-mcp@4.4.4` (pinned, so it does not change on its own). It needs no key and no sign-in. A free key from Context7's site raises its limits; they get it themselves (rule 5) | M | 64k |
| Claude | GitHub CLI, https://github.com/cli/cli | Lets your AI read GitHub pages from the terminal | `brew install gh` (they sign in with `gh auth login`) | B | 47k |
| Claude | Everything Claude Code, https://github.com/affaan-m/ECC | A big starter set of helpers, skills and hooks | `npx ecc-universal@2.2.3 setup` (it asks before it changes anything). It adds the Claude Code plugin ecc@ecc. Undo: `/plugin uninstall ecc@ecc`. Then, in the same folder, run `npx ecc-universal@2.2.3 uninstall --dry-run` to list anything else it wrote, and `npx ecc-universal@2.2.3 uninstall` only on their yes | P | 300k |
| Claude | Helper plugins, https://github.com/wshobson/agents | Ready-made helpers by job: coding, testing, writing | `/plugin marketplace add wshobson/agents`, then `/plugin` to pick | P | 42k |
| Claude | Graphify, https://github.com/Graphify-Labs/graphify | Turns a folder of files into a map your AI can search | `uv tool install graphifyy` (needs uv) | G | 145k |
| Claude | Ponytail, https://github.com/DietrichGebert/ponytail | Keeps the code your AI writes short and simple | `/plugin marketplace add DietrichGebert/ponytail`, then `/plugin install ponytail@ponytail`. It stays on in every session and shows a cost band above the prompt. `/ponytail off` turns it off | P | 188k |
| Claude | pstack, https://github.com/michael-denyer/pstack-claude | A tough code review your AI runs on its own work | `/plugin marketplace add michael-denyer/pstack-claude`, then `/plugin install pstack@pstack-claude`. It adds a hook that steers bigger tasks to its skills at the start of every session. Its setup-pstack skill turns that off | P | 4.2k |
| Claude | Claude cookbooks, https://github.com/anthropics/claude-cookbooks | Anthropic's recipes for builders. Running them needs a paid API key | `git clone https://github.com/anthropics/claude-cookbooks` | C | 54k |
| Claude | Sandbox runtime, https://github.com/anthropics/sandbox-runtime | Runs a command with limits on files and internet. For builders | `npm install -g @anthropic-ai/sandbox-runtime` | G | 7k |
| Claude | Warp plugin, https://github.com/warpdotdev/claude-code-warp | Claude Code alerts inside the Warp terminal. Only if they use Warp | `/plugin marketplace add warpdotdev/claude-code-warp`, then `/plugin install warp@claude-code-warp` (needs jq: `brew install jq`). Then restart Claude Code or run `/reload-plugins` | P | 0.2k |
| Many jobs | amux, https://github.com/mixpeek/amux | Runs several AI jobs at once from one dashboard or your phone. Needs tmux | `curl -fsSL https://amux.io/install.sh \| bash`. One of the smallest tools here, so show them the script and let them read it before it runs (rule 4). It copies amux into a new amux folder inside a Dev folder in their home folder. Its data goes in a hidden .amux folder there. It builds amux from source with Rust. If Rust is missing, it stops and names rustup, another internet script (rule 4). It adds three services that start at login and run a local server. Undo: in the amux folder, run `./uninstall.sh`. Then run `launchctl bootout gui/$(id -u)/com.amux.fleet-start` and move com.amux.fleet-start.plist from Library/LaunchAgents to the Trash. Then move the amux and .amux folders to the Trash, plus amux, amux-remote, amux-cloud and scripts/amux-grid.sh in .local/bin if they are there | S | 0.6k |
| Many jobs | Orchestrator, https://github.com/OrchestratorInc/agent-orchestrator | A desktop app that runs a team of coding AIs on one project | Download the app from its Releases page | A | 14k |
| Many jobs | AWS terminal orchestrator, https://github.com/awslabs/cli-agent-orchestrator | Lets one AI hand work to other AIs in the terminal | `uv tool install git+https://github.com/awslabs/cli-agent-orchestrator.git@main` (needs uv, and tmux 3.3 or newer) | G | 1.5k |
| Many jobs | Orchestrator list, https://github.com/andyrewlee/awesome-agent-orchestrators | A list of tools like these to compare | Open the page | R | 2.4k |
| Terminal | Ghostty, https://github.com/ghostty-org/ghostty (start) | A fast, easy-to-read terminal app | `brew install --cask ghostty` | B | 64k |
| Terminal | tmux, https://github.com/tmux/tmux | Keeps terminal jobs running in tabs after you close the window | `brew install tmux` | B | 50k |
| Terminal | tmux plugin manager, https://github.com/tmux-plugins/tpm | Adds tmux plugins with one key | `git clone https://github.com/tmux-plugins/tpm "$HOME/.tmux/plugins/tpm"`. Then add two lines to the bottom of their tmux settings file, .tmux.conf in their home folder (rule 9): `set -g @plugin 'tmux-plugins/tpm'` and, as the very last line, `run "$HOME/.tmux/plugins/tpm/tpm"`. If tmux is already running, `tmux source "$HOME/.tmux.conf"`. Undo also deletes those two lines and moves the tpm folder in .tmux/plugins to the Trash. If the run line fails with "returned 127", add `set-environment -g PATH "/opt/homebrew/bin:$PATH"` above it. It puts Homebrew first and keeps the folders already there. On an Intel Mac, use the folder that `echo "$(brew --prefix)/bin"` prints instead. Undo removes it too; tmux keeps the added folder until every tmux session is closed | C | 15k |
| Terminal | tmux-resurrect, https://github.com/tmux-plugins/tmux-resurrect | Brings your tmux tabs back after a restart | Needs the plugin manager first. Add `set -g @plugin 'tmux-plugins/tmux-resurrect'` to their tmux settings file, .tmux.conf in their home folder, above the plugin manager's run line (rule 9). Then, inside tmux, press the prefix (Control and b, unless they changed it), then capital I, to install it. To save their tabs before a restart, press the prefix, then Control and s. To restore after a restart, press the prefix, then Control and r. Undo: delete the line and move the tmux-resurrect folder in .tmux/plugins to the Trash | C | 13k |
| Terminal | tmux-continuum, https://github.com/tmux-plugins/tmux-continuum | Saves your tmux tabs every 15 minutes, on its own | Needs the plugin manager and tmux-resurrect first. Add `set -g @plugin 'tmux-plugins/tmux-continuum'` to their tmux settings file, above the plugin manager's run line (rule 9). Then, inside tmux, press the prefix, then capital I, to install it. To restore on its own when tmux starts, also add `set -g @continuum-restore 'on'` (rule 9). Undo: delete its lines and move the tmux-continuum folder in .tmux/plugins to the Trash | C | 4.1k |
| Posting | Postiz, https://github.com/gitroomhq/postiz-app | Schedules social posts, with a connection for your AI. Never posts unless they post (rule 6) | Self-host from the repository, which is free. The hosted version at postiz.com is a paid plan after a 7-day free trial, so say that first (rule 7) | R | 41k |

### Step 4. Tell them what they have now

Close with a short list:

- Each tool set up, what it added and where, and the check result.
- The undo line for each.
- One thing to try first with each, in their words, like "Ask Claude: add smooth scrolling to my home page with Lenis."
- Anything skipped, and why.

If they come back later and say "set up my toolkit" again, check what is already installed first and skip it.

Tell them to rename this chat "GITHUB" so it's easy to find.

---

## About me

I'm Eugeen, chief operating officer of a construction company in New York, with more than 90 employees. I built my AI setup over thousands of reps, for a real company, and I hold nothing back.

I check GitHub before I build anything. Some of the smartest coders in the world give their work away there for free, and a lot of what makes my AI fast came from it.

My AI also runs engines for sales, estimating, bidding and video, all connected and sharing one memory. I call the whole system Jarvis. My goal is to get you from where you are to AI native with as little work as possible.

**One free next step:** the quiz at bernan.ai/score shows what to set up next with AI in your business.




