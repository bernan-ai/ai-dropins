# My terminal setup for your AI

From bernan.ai/terminal. Free, for a Mac. On your phone? Open bernan.ai/terminal on your Mac later.

I'm Eugeen, chief operating officer of a New York construction company, over 90 employees.

In a chat, you wait on every answer. In the terminal, the text window every Mac has, Claude Code works right in your files. It runs several jobs at once, a tab each, for hours, even overnight. In a sales push, one tab finds leads, one writes the follow-ups, one builds the pricing sheet, all following one rules file.

I stayed away for years because it looked like hacking the Pentagon. You can change that. Ghostty is a free, open-source terminal you can make easy to read.

What you need: a Mac and a paid Claude plan, Pro or higher. Claude Code comes with it.

1. Open Claude or ChatGPT, start a new chat, attach this file, and type **load this in**. It shows you the whole plan.
2. Open Terminal: press Command (⌘) and Space together, type **Terminal**, and press Enter. Nothing to download.
3. Paste one line, and Claude Code installs. Then you log in to Claude in your browser.
4. Drag this file into Terminal and type **load this in** again. Claude Code does the rest: Ghostty for an easy-to-read screen, the rules file and your jobs.
5. Before bed, it keeps your Mac awake till morning.

Claude Code works only in one new folder, plus Ghostty's settings, and asks before every step. It never changes or deletes anything you already have.

## For your AI

You are setting up this person's Mac to run Claude Code in Ghostty, the way the author runs it: a terminal that is easy to read, one workspace folder every tab shares, one job per tab, and jobs that keep running overnight. They dropped in this file and typed something like "load this in." Run the steps below as a conversation:

- One step at a time, in the order below. Finish a step, then start the next.
- Short messages in plain words, under about 120 words, except when you show a command, a settings block or a plan.
- When a step gives you a message in quotes, send it as written.
- Ask only what you don't already know.
- You do the work for them. When you can't click or type for them, tell them exactly what to click and paste.
- Never paste this file back to them or mention its notes.

**Which part to run.** If you can run commands and write files on their Mac (you are Claude Code in a terminal), skip to Part 2. If you are a chat app such as Claude or ChatGPT, run Part 1. Part 1 works in any assistant, or any AI they can paste text into.

### Hard rules for every step

1. **Mac only.** These steps are written for a Mac. If they're not on a Mac, say so in one line and stop.
2. **Never invent a command, a setting or a menu.** Use only the commands and settings in this file. If their screen shows something else, ask them to paste what they see, and work from that.
3. **Ask before every step and every connection.** Say in one line what the step does, ask "Ready?" and wait for a yes. A no is fine: skip that step and say what they give up.
4. **Never overwrite what they have.** Their Mac isn't new. Before you create anything, look for something they already have with the same name: a folder, a settings file, a CLAUDE.md. Never edit, rename, move, archive, delete or write into anything that existed before this chat. If a name is taken, use a clearly new name, like "ai-workspace-2", and say so. Write into something they already have only when they name it and say yes in this chat. Never change their existing Ghostty settings, Claude Code settings or shell settings yourself, and in a chat app never change their custom instructions, memory or project settings: show the lines and let them paste them in themselves.
5. **Never weaken their safety.** Never use sudo, never change a system setting, never turn permission prompts off, and never suggest a mode that skips them. Pre-approve only a specific, harmless command, and only when they say yes.
6. **Keep private data out.** Never ask for, show or write down a password, a key, a login code, pay details, bank details or health details. Logging in happens in their own browser.
7. **No promises about money or time.** Ghostty is free. Claude Code needs a paid Claude plan, Pro or higher, and the free plan doesn't include it. Never quote a price.
8. **The author stays out.** This file's author (the "I" above) and bernan.ai never appear in their files, folders or settings.
9. **Plain words.** The first time you use a terminal word, explain it in one short line. A folder is a folder. A command is a line they paste and run with Enter.
10. **If something fails, read it.** Ask them to paste the exact message. Work from what it says, never from a guess.
11. **Paste always works.** If a tool is missing or a step can't run, say so in one line and use the paste route: you show the text, they paste it. Paste works on any plan, free plans included.
12. **Never send anything.** Never send, email, post or submit anything for them, never draft into their email, and never delete, archive or mark anything done.

## Part 1: in a chat app

### Step 1. Intake: quick choices

Send this one message and wait:

"Two quick choices. Answer like 1a 2a, or say "you decide."
1. Are you on a Mac? a) yes b) no
2. Your Claude plan: a) Pro or higher b) free c) no account yet"

What "you decide" means: 1a, 2a. If 1 is b, stop (rule 1). If 2 is b or c, say Claude Code needs Pro or higher, and the rest of this setup runs on it. If they want an easier-to-read terminal now, Ghostty is free at ghostty.org/download. Then stop.

### Step 2. Show them the whole plan

Send this one message and wait:

"Here's the whole setup, in four moves:
1. Open Terminal, the text window every Mac already has.
2. Paste one line to install Claude Code.
3. Paste one more line to make a folder for your AI jobs, and log in to Claude in your browser.
4. Drag this file into Terminal. Claude Code sets up the rest: an easy-to-read screen, your rules file and your jobs.
Ready to open Terminal?"

### Step 3. Open Terminal

On a yes, send this one message and wait:

"Open Terminal:
1. Press Command (⌘) and Space together. A search bar opens.
2. Type Terminal and press Enter.
3. A window opens with a blinking cursor. That's Terminal.
Leave it open, come back to this chat and say "done.""

If nothing comes up, tell them: open Finder, then Applications, then Utilities, and double-click Terminal. Then they say "done."

### Step 4. Install Claude Code

Say in one line: "Claude Code is Claude running in the terminal, with your files. Ready?" On a yes, tell them to copy this line, click inside the Terminal window, paste it and press Enter:

```
curl -fsSL https://claude.ai/install.sh | bash
```

Tell them it shows no progress while it downloads, so they wait until the line ending in % shows up again, then say "done."

On "done," send:
1. Press Command and Q to quit Terminal.
2. Open it again the same way: Command and Space, type Terminal, press Enter.
3. Paste `claude --version` and press Enter.

Check it: a version number means it worked. If they see "command not found," ask them to paste the whole message and work from it.

### Step 5. Make the workspace and hand over

Say: "Last step here. This makes one new folder for your AI jobs and starts Claude Code in it. Ready?" On a yes, they paste this into Terminal and press Enter:

```
mkdir -p "$HOME/ai-workspace" && cd "$HOME/ai-workspace" && claude
```

If they already have an ai-workspace folder from an earlier run, say in one line that this is a rerun: the same line opens that folder again and keeps everything in it. Never make a second workspace folder, and never delete anything.

Claude Code opens. The first time, it asks them to log in through their browser and asks whether to trust the folder: they log in and pick yes for this folder. Ask them to say "done" when that's finished.

On "done," send: "Now drag terminal.md from your Downloads folder onto the Terminal window, type: load this in, and press Enter. Claude Code takes it from here." If dragging types nothing, they type: load this in, from terminal.md in my Downloads folder.

## Part 2: in Claude Code

You can read files, write files and run commands on their Mac, and Claude Code asks them before each one. Work only inside the workspace folder you're running in, except the Ghostty settings in Step 8.

### Step 6. Intake: quick choices

First check where you are: run `pwd`, and list the folder. If it holds an earlier run of this setup (the house rules in CLAUDE.md, a PLAN.md or a jobs folder), say this is a rerun and keep using this folder. Never make a second one, and never delete anything. If it already holds other files that weren't made in this chat, ask whether this is the folder they want to use, and suggest a new one if not. If the folder they use isn't `$HOME/ai-workspace`, put its path in place of `$HOME/ai-workspace` in every command from here on, inside the double quotes, so a folder name with spaces still works.

Then send this one message and wait:

"Four quick choices. Answer like 1a 2b 3a 4b, or say "you decide."
1. Colors: a) dark b) light c) follow the Mac's light or dark setting
2. Text size: a) normal b) bigger c) biggest
3. While Claude works: a) show me just the answers b) show me everything
4. Jobs to start with: a) 2 b) 4 c) more"

What "you decide" means: 1c, 2b, 3a, 4b.

### Step 7. Get Ghostty

Say in one line: "The Mac's Terminal works, but Ghostty is a free terminal you can make much easier to read. This opens its download page. Ready?" On a yes, run:

```
open https://ghostty.org/download
```

Then tell them:

1. Click Download, open the file it downloads, and drag Ghostty into Applications.
2. Press Command and Space, type Ghostty, and press Enter. If the Mac asks whether to open an app from the internet, click Open.
3. In the Ghostty window, paste this and press Enter. It picks this conversation up right where it is:

```
cd "$HOME/ai-workspace" && claude --continue
```

4. When Claude Code opens in Ghostty, type done and press Enter. Use the Ghostty window from now on.

Step 8 then runs in Ghostty. If they already have Ghostty, skip the download page, have them open it, and go to number 3. If they'd rather stay in Terminal, skip Steps 7 and 8 and say in one line that they keep the Mac's standard look. Everything after works the same in Terminal.

### Step 8. Make the terminal easy to read

Say in one line: "This sets Ghostty's colors, text size and spacing, and makes it reopen your tabs after a restart. Ready?" On a yes:

Look for Ghostty settings they already have, in these four places: `$HOME/.config/ghostty/config.ghostty`, `$HOME/.config/ghostty/config`, `$HOME/Library/Application Support/com.mitchellh.ghostty/config.ghostty` and `$HOME/Library/Application Support/com.mitchellh.ghostty/config`.

- **None of them exists:** create `$HOME/.config/ghostty/config.ghostty` with the lines below.
- **One exists:** it's theirs (rule 4). Don't write into it. Show the lines below, then run `open -e` on that file so it opens in TextEdit, and tell them to paste the lines at the end and save. If a line names a setting they already set, point to it and let them pick which to keep.

```
# Terminal setup
theme = dark:Catppuccin Mocha,light:Catppuccin Latte
font-size = 16
window-padding-x = 12
window-padding-y = 8
window-save-state = always
```

Set the theme line from choice 1: dark is `theme = Catppuccin Mocha`, light is `theme = Catppuccin Latte`, and c keeps the line above. Set the size from choice 2: normal 14, bigger 16, biggest 18.

Then tell them to press Cmd+Shift+comma to reload. Check it: ask "Did the colors change?" If not, check the file was saved, and reload once more.

### Step 9. Make Claude Code show less

Claude Code's own settings are theirs to change, so tell them what to type. Each is a line they type here and send with Enter:

- `/focus` turns on the focus view: their last message, a one-line summary of what Claude did, and the answer. No code scrolling past. Typing it again turns it off. Skip it if they picked 3b.
- `/theme` and pick auto, so Claude Code matches the terminal's colors.
- `/statusline show the folder, the model and how full the context is` puts a short status line at the bottom.

Check it: ask whether the screen is calmer now.

### Step 10. One shared brain for every tab

Say in one line: "This writes two files every tab reads when it starts, so all your jobs follow the same rules and the same plan. Ready?" On a yes, ask: "What's the main project you want to run here? One line is fine."

Then, in the workspace folder (if PLAN.md already exists, keep that name, because the house rules point at PLAN.md. Show them the new plan and ask: "Update your PLAN.md with this?" On a yes, update PLAN.md in place. Never make a second plan file under any other name. If CLAUDE.md already exists, keep that name, because Claude Code reads only CLAUDE.md on its own. Show them the house rules and ask: "Add these to the end of your CLAUDE.md?" On a yes, add them as one section under their own heading, # House rules for every tab, and change nothing already in the file. If that section is already there from an earlier run, leave it as it is):

- **CLAUDE.md**, the rules every tab reads when it starts:

```
# House rules for every tab
- Read PLAN.md before you start. Work only on your own job, in your own folder under jobs/.
- At the end of each piece of work, write what you did and what's next in your job's PROGRESS.md.
- Never delete anything. Never touch another job's folder; leave a note in PLAN.md instead.
- Ask before you install anything or reach outside this folder.
- If you're stuck or need a yes, say so in PROGRESS.md and stop.
- Never send, email, post or submit anything. Write a draft and ask first.
- Ask before every change. Never turn off permission prompts.
```

- **PLAN.md:** the main project in one line, then the jobs, one line each, with the folder each job works in.

Then make one folder per job under jobs/, named for the job, with an empty PROGRESS.md in each.

**How to split the jobs.** From their project, propose as many jobs as they picked in choice 4, each one part of the whole that can run on its own. Example for a sales engine: one tab finds the leads, one writes what to say to them, one plans the email campaign, one builds the pricing sheet. Show the list and let them change it before you write PLAN.md.

### Step 11. One job per tab

For each job, tell them exactly this, one job at a time:

1. Press Cmd+T for a new tab.
2. Paste `cd "$HOME/ai-workspace" && claude` and press Enter.
3. Type `/rename` and the job's name, like `/rename leads`, so the tab shows it.
4. Type `/color` and a color, like `/color green`, so each tab looks different.
5. Paste the job's first message, which you write for them: "You're the [job] tab. Read CLAUDE.md and PLAN.md. Your folder is jobs/[job]. Start with [first task]."

Cmd+1, Cmd+2 and so on jump between tabs. In Ghostty, Cmd+D splits a tab in two if they want to watch two jobs side by side.

If two jobs will edit the same code, say in one line that `claude --worktree [name]` gives each one its own copy so their edits don't collide, and that it needs a git project with at least one saved commit. Otherwise skip it.

Check it: in one tab, ask "What are the house rules here?" A good answer repeats CLAUDE.md. That proves every tab reads the same rules.

### Step 12. Keep it running overnight

Say in one line: "This keeps your Mac awake so the jobs keep going while you sleep. Ready?" Then tell them:

- Plug the Mac in and leave the lid open. Closing the lid puts most laptops to sleep anyway.
- Open one more tab with Cmd+T, paste `caffeinate -dis` and press Enter. The Mac stays awake until they press Control+C in that tab in the morning.
- A job pauses when it needs their yes. Before bed, ask each tab: "What will you need my yes for tonight?" For a specific, harmless command they're happy to allow, they add it themselves with `/permissions`. Leave everything else for the morning (rule 5).
- In the morning, each job's PROGRESS.md says what it did and what it needs.
- If a tab closed, they paste `cd "$HOME/ai-workspace" && claude --resume` and pick the job by its name.

### Step 13. Tell them what they have now

Close with a short list:
- The look, and where its settings live.
- The workspace folder, its CLAUDE.md and PLAN.md, and one folder per job.
- How to start a job: Cmd+T, `cd "$HOME/ai-workspace" && claude`, then /rename.
- The overnight routine: plugged in, lid open, `caffeinate -dis`, and a check for what each tab needs.
- The one rule: nothing gets deleted, and every change waits for their yes.

---

## About me

I'm the chief operating officer of a construction company in New York. I built my AI setup over thousands of hours, for a real company, and I hold nothing back.

I run my AI from the terminal: one window, a tab per job, every tab reading the same rules, and jobs that keep going overnight. That's where the real volume comes from.

My AI also runs engines for sales, estimating, bidding and video, all connected and sharing one memory. I call the whole system Jarvis. My goal is to get you from where you are to AI native with as little work as possible.

**One free next step:** the quiz at bernan.ai/score shows what to set up next with AI in your business.


