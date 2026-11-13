---
name: codes
description: Price a trip's rental car and hotel with every discount code the user can honestly use. Reads the trip from their calendar, prices Avis, Hertz and Enterprise side by side with a child seat if asked, prices Hilton with public rates and codes, shows one table, and books only the row they pick after they say go. Use for price my trip, rental car, car with a car seat, Avis code, Hertz code, Hilton rate, discount code, book a car, book a hotel.
---

# codes

A trip goes in. One table comes out: company, car or room, code, and the total with taxes and extras. Nothing is booked until you say go.

## Install, once

1. You need Claude Code, the version of Claude that runs on your computer.
2. Put this folder in your Claude skills folder as `codes`. On a Mac that is `~/.claude/skills/codes`. Or ask Claude Code: "Install the codes skill from github.com/bernan-ai/ai-dropins, folder codes/skill."
3. Put [codes.md](../codes.md) in the same folder. It holds the method and the code lists.
4. Check the math script with `python3 compare.py check` from this folder. It needs only Python.

No key and no account beyond Claude Code. The script sends nothing anywhere.

## Use

Type **price my trip**, or type the trip: "Chicago O'Hare, Dec 4 to 7, a car with a child seat, one Hilton room."

## Undo

- Nothing you have changes. The skill reads your calendar and never edits it. It never saves a code to your travel profiles.
- A booking it made on your go is cancelled the usual way, on that company's site, under its cancel rule.
- Delete this folder to remove the skill.

## For Claude

Read `codes.md` in this folder, from "## For your AI" down, and run it as written: the hard rules, the intake, the plan, the connections, the pricing, the table and the booking. Here, in Claude Code:

1. **Calendar.** Use a calendar tool or connector they already have. If none, ask them to paste the flight confirmation. Read only.
2. **Browser.** Use the Claude in Chrome extension or a browser tool they already have, in their own browser where they are signed in. Car sites often block a background browser; if a site shows a human check, ask them once to tick it, then run every code in that same session.
3. **Math.** Write each price you read into `quotes.csv` in a new folder named `trip-` plus today's date, then run `python3 compare.py table --quotes <that folder>/quotes.csv`. Show the table it prints. Never add a total in your head.
4. **Book.** Only on "go" and a row number, as Step 6 of codes.md says.

Rules:

- Never invent a price or a code. A total comes only from a page you read.
- Never type, print or save a password, card number or member number.
- Never overwrite or delete their files, events or profiles. Work only in the new trip folder.
- Never say a booking exists unless you read it on the company's own page.
