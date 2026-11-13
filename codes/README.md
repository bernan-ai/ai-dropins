# CODES: price your rental car and hotel with every discount code

The file is [codes.md](codes.md). It works in Claude or ChatGPT, free plans included.

## How to use it

1. Download [codes.md](codes.md). It's a plain text file. On an iPhone it lands in Files, then Downloads.
2. Open Claude or ChatGPT and start a new chat. Tap + or the paperclip and attach the file.
3. Type **price my trip**, or type the trip, like: "Chicago O'Hare, Dec 4 to 7, a car with a child seat, one Hilton room."
4. Answer up to four quick choices, or say "you decide": where the trip is, what car and child seat, which hotel, and which codes you can use (public only, AAA, your Amex card, or your employer's). It skips any you already typed. "You decide" uses public codes only.
5. It shows you the plan, then offers two connections, one at a time. Your calendar, so it reads your flight times instead of you typing them. And a browser it can use for you, like the Claude in Chrome extension or ChatGPT's own browser mode, where you sign in to Avis, Hertz and Hilton so your member rates show. It gives you the clicks. Say no to either and you paste instead.
6. You get one table: Avis, Hertz and Enterprise side by side, then Hilton, each with the code used, the total with taxes and extras, and the cancel rule.
7. Pick a row and say go, like "go 2" for row 2. Nothing is booked before that.

It tries only the codes you said you can use. Searching a booking site with a code books nothing.

The [skill folder](skill/) is optional, for people who use Claude Code, the version of Claude that runs on a computer. Skip it otherwise. Its small script adds up the totals on your computer and sends nothing anywhere.

## The codes inside

All of them are in [codes.md](codes.md), under "The code lists", each with its public source and the day it was checked.

| List | What it is |
|---|---|
| Avis public codes | Avis discount codes (Avis calls them AWD numbers) and coupons published for anyone to use |
| AAA members | Where to find your AAA code at Hertz and the AAA rate at Hilton |
| American Express cardmembers | Avis and Hertz codes from public pages, plus the free member status the Platinum Card gives at Hilton, Avis and Hertz once you enroll. Only if you hold the card |
| Enterprise | No public code we could verify, so it's priced at its plain rate, for comparison |
| Company codes | Hilton corporate codes, behind a warning. Only if you work there |

Company codes are used only if you name your employer in choice 4. They carry a real risk. A front desk or rental counter can ask for proof you work there. A wrong-code rental can be repriced or voided. Avis can put a renter on its do-not-rent list. Use public codes first.

Codes change. A code the site rejects is dropped from the table.

## What changes in your accounts

- **Your calendar:** nothing. Your AI only reads it, and only if you connect it.
- **Your Avis, Hertz, Enterprise and Hilton accounts:** nothing, until you say go on one row. Then it books that one reservation. It never saves a code to your profile, and never changes or cancels a reservation you already have.
- **Your AI:** nothing. It never changes your custom instructions, memory or settings.

You sign in yourself. After you say go, your AI fills in the booking up to payment, you type payment yourself, then it presses the final book button only if the total matches the table. Pay now and pay later both show in the table, and a pay now row gets a warning first. Your AI is told never to type, copy or save your password or card number.

On a free plan, or with no browser connected, it still works: your AI gives you the links and codes, you paste back the prices, and you book the row yourself. Letting it use a browser needs a plan that has that feature.

## What this reads, writes and sends

- **Reads:** the trip you type or paste, and, if you connect them, your calendar and the booking pages in a browser where you're signed in.
- **Writes:** one table in your chat. One booking, only after you say go on that row. The skill writes a quotes file in a new folder.
- **Sends:** no email, text or post. In ChatGPT or Claude, what you share goes to that app under its terms. The skill's script sends nothing anywhere.

## Undo

- Cancel a booking on that company's site, under its cancel rule. Pay later rates usually cancel free; pay now rates often don't.
- Disconnect your calendar or the browser in your AI app's settings.
- Delete the file, or the skill folder, to remove it.

Everything here is as is, with no warranty, and it is not professional or travel advice. Codes were checked on Nov 12, 2026. Prices come live from the booking sites each time. The license is on the [main page](../README.md).
