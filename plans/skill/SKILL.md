---
name: plans
description: Turn a plan set (PDF or sheet images) into a first-pass takeoff. Names and shades every room, marks and counts every door, lists floor, wall and ceiling square feet, base linear feet and fixture counts by room, flags what it is unsure of, and prices it from the user's own rate sheet. Use for run my takeoff, take off this plan set, count the doors, how many square feet, price this plan set.
---

# plans

A plan set goes in. A marked-up plan, a takeoff, a flag list and a first-pass price come out. Claude reads the sheets. A small script on your computer re-adds every column, draws the marked-up plan and does the price math.

## Install, once

1. You need Claude Code, the version of Claude that runs on your computer.
2. Put this folder in your Claude skills folder as `plans`. On a Mac that is `~/.claude/skills/plans`. Or ask Claude Code: "Install the plans skill from github.com/bernan-ai/ai-dropins, folder plans/skill."
3. For the marked-up plan the script needs Pillow. Check with `python3 plan_tool.py check` from this folder. It says what is missing.
4. Copy [example-rates.csv](../examples/example-rates.csv) and put in your own rates. The example rates are made up.

No key and no account beyond Claude Code. The script sends nothing anywhere.

## Use

Type **run my takeoff** and drop in the plan set and your rate sheet.

## Undo

- Your plan set never changes. Every output is a new file in a new folder beside it.
- Delete this folder to remove the skill.

## For Claude

Run these steps as a short conversation. Plain words, short messages.

1. **Set.** Ask for the plan set and their rate sheet. Make a new folder beside the plan set named `takeoff-` plus today's date, and work only in it. A PDF: turn each page into a PNG in that folder, about 2400 pixels wide, with any tool on the machine. Never edit their files.
2. **Read.** Open every sheet. List each sheet, its title and scale, and whether the set has a finish schedule, a door schedule and a ceiling plan. Then write `takeoff.json` in the new folder:
   - `rooms`: number, name, floor_sf, floor_sf_source (printed, schedule or worked out from dimensions), perimeter_lf, ceiling_height_ft, wall_sf (perimeter x height, openings not deducted), ceiling_sf, base_lf (perimeter minus door openings), floor_finish, and `box`: the room's rough outline on the floor plan image as [x0, y0, x1, y1], fractions of the width and height from the top left.
   - `doors`: mark, room, width, type, leaves (a pair is 2), and `at`: [x, y] on the same image.
   - `fixtures`: item, room, count. Only what is drawn. No ceiling plan means no light count.
   - `flags`: where, reason. One for every place you are unsure.
   - `totals`: floor_sf, wall_sf, ceiling_sf, base_lf, doors.
   Never guess a number. A missing area, height or count is a flag and a blank.
3. **Re-add.** Run `python3 plan_tool.py totals --takeoff <folder>/takeoff.json`. Any slip it names, fix in the JSON from the sheet, then run it again.
4. **Mark up.** Run `python3 plan_tool.py markup --takeoff <folder>/takeoff.json --plan <the floor plan PNG>`. Open the picture. Check every room is shaded on the right room and every door dot sits on a door. Move a box in the JSON and rerun if not.
5. **Price.** Only with their rate sheet: `python3 plan_tool.py price --takeoff <folder>/takeoff.json --rates <their rates.csv>`. A rate row's `quantity` is one of floor_sf, wall_sf, ceiling_sf, base_lf, doors, markup_pct, or `fixture:<item name>` to price a counted fixture.
6. **Show.** The flags first, then the room table, then the totals, then the price with its "FIRST PASS, NOT A PRICE TO SEND" line, then the marked-up plan.

Rules:

- Never invent a rate, a price or a measurement.
- Price only through the script, never by mental math.
- Never overwrite or delete their files. The script refuses to overwrite its own outputs.
- Never say a file exists unless the script printed "saved".
- A takeoff is a first pass. Say so every time: a person checks every number before it goes to a client.
