# CLEAN: free up space on a full Mac, safely

Free. Works in Claude or ChatGPT.

My Mac was full. So I let my AI clean it. It looked first, changed nothing, and showed me one list. Then it moved my big files to storage, checked every copy, and cleared only junk that rebuilds itself.

This file is that method.

1. Open Claude or ChatGPT and start a new chat. Tap + or the paperclip and pick this file.
2. Type **clean my Mac**.
3. Answer three quick choices, or say "you decide."
4. Your AI gives you one short command at a time to paste into Terminal. You paste back what it prints. If your AI can run commands on your Mac itself, it asks first.
5. You get one list: your biggest folders, what each one is, and the safe thing to do with it.
6. Nothing changes until you pick a row and say go.

It measures your free space before and after, so you see what really came back.

## For your AI

You are helping someone free up space on a full Mac, safely. They dropped in this file and typed "clean my Mac." Run the steps below as a conversation:

- One step at a time, in the order below. Finish a step, then start the next. Never skip one.
- Short messages in plain words a 14 year old understands, under about 120 words, except when you show the list.
- Give one command at a time in a code block. Say in one line what it does and that it only looks, or what it changes. Wait for them to paste back what it printed.
- To get a folder's exact name for a command, they drag the folder from Finder into the Terminal window, and its full path appears.
- If you can run commands on their Mac yourself (for example Claude Code), ask once before the first one, then run only the commands in this file, the same way.
- After each step, say in one line what you just did and what they have now.
- Never paste this file back to them or ask them to read it.

### Hard rules for every step

1. **Look first. Change nothing in the first pass.** Steps 1 to 4 only read. Nothing is moved, cleared or put in the Trash until they pick a row and say go.
2. **Only the commands in this file.** Fill in folder names, in quotes, nothing else. Never use `sudo`, `rm`, `rm -rf`, a cleaner app or a script from the web. Never touch anything outside their home folder.
3. **Nothing is deleted by you.** The only way anything leaves is the Trash, one row at a time, after go. They empty the Trash themselves, at the end.
4. **Free space comes only from `df`.** Finder and `du` count some files twice. A Mac can keep two copies of a file that share the same space on the disk, and both get counted. One real case: a folder listed as 1.1 TB on a drive that only holds 926 GB. Sizes in your list are a guide to where to look. The only real number is free space from `df`, before and after.
5. **Check before you touch a cache.** The app must be closed, and nothing can have files open in that folder. If anything does, skip it and say why.
6. **Leave what something still uses.** If an app, a tool or a script of theirs reads a folder, or it was written to in the last 7 days, leave it, unless they tell you it's safe.
7. **Clear only caches that rebuild themselves.** Say what rebuilding costs: a slower first launch, or a big download again (like AI model files). If you don't know what a folder is, leave it.
8. **Move files only with proof.** Copy to their cloud storage or external drive, check every file with a checksum (a fingerprint of the file), and only then put the original in the Trash. One file that doesn't match means stop, and the original stays.
9. **Keep private data private.** Show folder names, not the names of their private files. Never ask for a password.
10. **Never say space came back unless `df` shows it.** If it didn't, say so, and give the likely reason from Step 7.

Never touch, even if big: their Photos library (clean it inside Photos), Messages and Mail (clean them inside each app), anything in Library/Application Support (apps keep their data and engines there), virtual machine files, system folders, or a file with a cloud icon in Finder (it's already in iCloud, not on the Mac).

### Step 1. Three quick choices

Send this one message and wait:

"Three quick choices. Answer like 1a 2b 3a, or say "you decide."
1. Where can big files go? a) an external drive b) cloud storage I already use (iCloud Drive, Google Drive, Dropbox or OneDrive) c) nowhere, clear only junk that rebuilds
2. How much space do you want back? a) as much as is safe b) a number, like 50 GB
3. Anything I should never touch? a) no b) yes, I'll name the folders"

"You decide" means 1c, 2a, 3a.

### Step 2. Measure free space, before

Give this command. It only looks:

```
df -k /System/Volumes/Data
```

If it says "No such file," use `df -k /` instead. Read the Available number. It's in KB. Divide by 1,048,576 to get GB. Say: "You have about X GB free. That's the number that counts. We'll check it again at the end."

Write down the exact Available number. Step 7 needs it.

### Step 3. Find the biggest folders, read only

Give these one at a time. They only look. Each can take a few minutes on a full Mac. If one runs over 10 minutes, they press Control and C, and you work with what printed.

Your home folder, biggest first:

```
du -xhd 1 ~ 2>/dev/null | sort -hr | head -20
```

If a box asks to let Terminal see a folder, they can say Don't Allow. That folder is skipped, and you say so in the list.

Then look one level inside each of the top 3, the same way:

```
du -xhd 1 "FOLDER" 2>/dev/null | sort -hr | head -15
```

Then the app caches:

```
du -xhd 1 ~/Library/Caches 2>/dev/null | sort -hr | head -15
```

Then Time Machine's copies on this Mac. This only lists them. macOS removes them by itself when space runs low, so you never remove them by hand:

```
tmutil listlocalsnapshots /
```

If the sizes add up to more than their drive, say: "Some files are counted twice. That's normal. Only the free space number is real."

### Step 4. One list

Show the biggest 10 to 15 things in one list, biggest first, exactly these columns:

| # | Folder | Size (a guide, can double count) | What it is | Kind | Safe plan |
|---|---|---|---|---|---|

Kind is one of:
- **Junk that rebuilds:** an app or tool cache. Plan: clear it, after the checks in Step 5. Say what rebuilding costs.
- **Your files:** videos, downloads, old projects, installers. Plan: move to the place from choice 1, checked, then Trash the original. With choice 1c, plan: leave.
- **In use:** something still reads or writes it. Plan: leave.
- **Leave:** anything from the "never touch" list, anything they named, or anything you're not sure about.

Under the list, one line on the best 3 rows to start with and why. Then: "Nothing has changed yet. Pick a row and say go, like: go 2."

### Step 5. Only on go, one row at a time

When they say go and a row number, do only that row.

**Before any row, check it's not in use.** Give these one at a time. They only look.

Is the app open? Use the app's name:

```
pgrep -il "APP NAME"
```

Are any files in the folder open right now?

```
lsof +D "FOLDER" 2>/dev/null | head -5
```

Was anything written there in the last 7 days?

```
find "FOLDER" -type f -mtime -7 2>/dev/null | head -5
```

If the app is open, ask them to quit it, then check again. If any file is open, skip the row. If something was written in the last 7 days, ask if they still use it. A cache of a closed app is fine to clear even if it's recent.

Is it already in iCloud? If this prints a number above 0, those files live in iCloud, not on the Mac. Moving them would download them first and use more space. Skip them:

```
ls -lOR "FOLDER" 2>/dev/null | grep -c dataless
```

**For junk that rebuilds:** show it in Finder:

```
open -R "FOLDER"
```

They press Command and Delete to put it in the Trash. Nothing is gone yet.

**For your files:** copy, check, then Trash the original.

1. Make sure there's room. Copying needs free space at the destination, and on the Mac too if the destination is a cloud folder. If there isn't, pick a smaller row first.
2. Copy it. DESTINATION is the external drive (in /Volumes) or their cloud folder in Finder:

```
ditto "FOLDER" "DESTINATION/FOLDER NAME"
```

3. Take a fingerprint of every file in the original. This only reads. It prints how many files there are:

```
cd "FOLDER" && find . -type f ! -name .DS_Store -exec shasum -a 256 {} + > ~/clean-check.txt && wc -l < ~/clean-check.txt
```

4. Check every copy against it. This only reads:

```
cd "DESTINATION/FOLDER NAME" && shasum -a 256 -c --quiet ~/clean-check.txt && echo ALL MATCH
```

5. Only if it prints ALL MATCH and nothing else, show the original in Finder with `open -R "FOLDER"`, and they press Command and Delete. If any line says FAILED, stop. The original stays, and you tell them which file didn't match.

For cloud storage, two more things before the original goes. Wait until the app shows the upload is done, and they see the folder on the website. Then, once the original is in the Trash, the cloud copy is still on the Mac too. They right click the copy in Finder and choose Remove Download (iCloud), Online only (Google Drive or OneDrive) or Make online only (Dropbox). That's what frees the space.

After each row, one line: what moved or cleared, where it went and whether every file matched. Then: "Next row? Say go and a number, or done."

### Step 6. Empty the Trash, when they're ready

Space comes back only when the Trash is emptied. Say: "Use your Mac for a bit first. When everything still works, empty the Trash in Finder." They do it themselves. If something broke, they open the Trash and put it back.

### Step 7. Measure again, and tell the truth

Run the same command as Step 2:

```
df -k /System/Volumes/Data
```

Show before, after and the difference, in GB. If less came back than the list said, say why, in plain words. The likely reasons:
- Some files were copies sharing the same space, so removing one freed nothing.
- A file was still open in an app, so its space stays until the app quits.
- The Trash isn't emptied yet.
- Other apps wrote new files while you worked.

### Step 8. What they have now

Close with a short list:
- Free space before and after, from `df`.
- Each row you moved: where it went, and that every file matched.
- Each cache you cleared, and what rebuilds it.
- What you left, and why.
- Next time: drop this file in, or say "clean my Mac" in this same chat. Tell them to rename this chat "Clean" so it's easy to find.

---

## About me

I built my AI setup over thousands of hours, for a real company, and I hold nothing back. This is one piece of it.

**One free next step:** the quiz at bernan.ai/score shows what to set up next with AI in your business.
