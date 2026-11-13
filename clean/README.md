# CLEAN: free up space on a full Mac, safely

The file is [clean.md](clean.md). It works in Claude or ChatGPT, free plans included.

## How to use it

1. Download [clean.md](clean.md). It's a plain text file.
2. Open Claude or ChatGPT and start a new chat. Tap + or the paperclip and attach the file.
3. Type **clean my Mac**.
4. Answer three quick choices, or say "you decide": where big files can go (an external drive, your cloud storage, or nowhere), how much space you want back, and anything it should never touch.
5. Your AI gives you one short command at a time. Open Terminal (press Command and Space, type Terminal), paste it in, and paste back what it prints.
6. You get one list: your biggest folders, what each one is, and the safe plan for it.
7. Pick a row and say go, like "go 2". Nothing changes before that.

## How it stays safe

- **It looks first.** The first pass only reads. Nothing moves until you say go on one row.
- **It measures free space with `df`, before and after.** Finder and `du` can count the same space twice. One real case showed a 1.1 TB folder on a 926 GB drive.
- **It moves before it removes.** Your files are copied to your cloud storage or external drive, every file is checked by checksum, and only then does the original go to the Trash.
- **It checks what's in use.** Before a cache, it checks the app is closed and no file in the folder is open. Anything another app or tool still reads stays.
- **It clears only junk that rebuilds itself,** like app caches, and tells you what rebuilding costs.
- **It never deletes.** Everything goes to the Trash. You empty the Trash yourself, when you're sure.

## What this reads, writes and sends

- **Reads:** folder sizes in your home folder, and which apps and files are open, through commands you paste or approve.
- **Writes:** on go, a copy of a folder on your drive or cloud storage, and one small checksum list, `clean-check.txt`, in your home folder. Originals go to the Trash only after every file matches.
- **Sends:** nothing. In ChatGPT or Claude, what you paste goes to that app under its terms. Files you move to cloud storage go to that service, which you chose.

## Undo

- Before you empty the Trash, open it and choose Put Back on anything.
- A moved folder is still on your drive or cloud storage. Copy it back the same way.
- Delete `clean-check.txt` from your home folder.
- Delete the file to remove it.

Everything here is as is, with no warranty, and it is not professional advice. Back up anything you can't lose before you start. The license is on the [main page](../README.md).
