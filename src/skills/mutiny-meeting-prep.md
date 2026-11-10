---
name: mutiny-meeting-prep
description: "Mutiny meeting prep, from Sales Skills by Mutiny. So the rep walks into the call ready: a one-page brief they can read in a minute, covering who's attending, where the deal stands and what's still owed, what the buyer cares about in their own words, the questions to ask, what to leave the call with, and anything that could go wrong. Works for a first call and for the tenth, and finds the meeting on the calendar without being told which one. One call at a time; the daily brief covers the whole day. It's for the rep only and never goes to the buyer. Use whenever someone says 'Run the Mutiny meeting prep for [company]', 'prep me for my call with [company]', 'pre-call prep on [company]', 'what do I need to know before my next call', wants to get ready for a sales meeting, or wants prep done automatically before their meetings."
---


So they walk into every call ready. This is a brief for one upcoming call that they can read in 60 seconds before they join. It's for the rep. The buyer never sees it.

| Section | What it tells them |
|---|---|
| Attendees | Who's coming and each person's part in the decision, labeled only when it's earned |
| Where we are | What's happened so far, and what either side still owes |
| What they care about | Their pain, goals and numbers, in their words |
| Questions to ask | What the rep still needs to find out at this stage, written as questions |
| Leave with | 2–4 things to walk out of the call holding |
| Heads up | Real risks, each with a way to handle it |
| In their words | Phrases the buyer uses, worth saying back to them |

Why they're meeting goes at the top of the page. Every section is optional. A first call with no history might have three, and that's the right brief for it.

## Step 1: Find the call

Look at the next 14 days of the calendar for meetings with the company they named, and match each to a CRM deal.

- **One match.** Go straight on. Put the call in the page's headline so a wrong pick is obvious. Don't stop to confirm. Nobody has time for a round trip right before a call.
- **Several meetings on the same deal.** Prep the next one. Mention the later ones in a line of chat.
- **Meetings for different deals or groups at one company** (two business units, say). Ask which, with one line per option: date, time, attendees, deal. This is the only time you ask.
- **No company named.** Prep their next sales call: an external meeting with a buyer, prospect or customer, today or the next working day. You can tell by a CRM deal or contact, or a booking from a prospect. Skip vendors, partners, agencies, recruiting and personal meetings, though a partner or customer who booked through a sales or demo link counts as a sales call. Name what you skipped in a line of chat ("Skipped the 8:00 agency kickoff: not a sales call.").
- **The company they named is a vendor or partner** (they sell to the person, or there's no buyer relationship). Say so in `notes` and write a short brief: Attendees, Where we are, and Leave with. Drop the rest.
- **No match.** Say so in two lines with the likely reason (a different name on the invite, a calendar you can't see, not booked yet) and ask for the buyer's name or the meeting details.

## Step 2: Gather

Read widely, then keep only what helps on this call. The reading budget:

- **CRM.** The deal (stage, amount, close date, next step, source, owner, any custom fields that are filled in) and each attendee's contact record. Notes and the last 15 activities. Any form submission that created the contact.
- **Call recordings.** Summaries of every earlier call with this company, however old, and full transcripts of the latest one or two. Prep builds up over time: the first calls usually hold the buyer's original goal, what success means to them and their early doubts, and all of that matters on every call after.
- **Email.** Threads with each attendee from the last 90 days, read to the end. Include replies from teammates the person was copied on and emails the deal owner logged in the CRM. Before you call anything owed, check that nobody on the team already answered it. For a first call, read the thread that booked it closely. Buyers often state their goal or timeline there, and by call time everyone has forgotten.
- **Chat, if it's connected.** Direct messages with attendees, and internal threads about the deal.
- **Contracts, if connected.** Documents that are pending and where each signature stands.
- **Web.** A quick look at any attendee with no CRM or call history: their role and how long they've been there. Company news only when it connects to something the buyer said matters.

Then work out two things. First, which call this is with the buyer, counting real meetings. Second, whether the buyer has given you anything yet, such as a booking form, a reply to the intro, SDR handoff notes or earlier calls. A first call with a filled-in form isn't a blank slate.

## Step 3: Check it against the profile

This step is the difference between a recap and prep. Use the profile files (see the shared context):

- **What they still need to find out.** Take how they qualify from `mutiny-sales-process.md` under `## Discovery and qualification` (MEDDIC, SPICED, BANT or their own), and what the deal's current stage needs from `## Pipeline stages`. For each element, decide from the evidence whether it's known, partly known or unknown. The unknowns that matter at this stage become Questions to ask. With no profile, use what any solid discovery checks (budget, who decides, timeline, the problem, the competition) and say that's what you used.
- **Best-deal moves.** If `mutiny-how-i-work.md` lists moves under `## What I do on my best deals`, work the one that fits into Leave with ("On your best deals you get the person who signs on a call before the pilot starts.").
- **What slips.** Check this deal against each item under `## What slips`, and raise the ones that apply under Heads up.
- **Competitors.** If one came up, use `mutiny-buyers-and-competitors.md` for how they usually win or lose against it.
- **Is the deal going quiet?** It is if there's been no two-way touch in 14 or more days, there's no next step, or a promised next step didn't happen. If so, say it in `alert`.

## Step 4: Build the page

The brief is a page with a fixed design. Copy the template under `## Report template` at the end of this file exactly and replace only the `DATA` object. Don't restyle it or write your own HTML. Use the sections below in this order, so the person finds things in the same place before every call. Leave out a section when you have nothing real to put in it.

Show the page as an artifact. If you can't, save the filled template as `meeting-prep-[company].html` and share the file. Only when you can't show or save HTML at all, write it as Markdown: the same sections in the same order, each title as a `##` header and each row as one bullet ending in its source. The first time someone runs this, add one line in chat: "You'll get this same page before every call. 'How this page works' at the bottom explains each section."

**Top of `DATA`:**

| Field | What goes in it |
|---|---|
| `kind` | "Meeting prep" |
| `title` | The buyer's company and the kind of call: "Vantage pricing sync" |
| `sub` | When, and which call this is: "Tue Oct 6 · 11:00am · 45 min · Call 3" or "... · First call" |
| `notes` | Up to three short lines: "Agenda: ..." from the invite; "They want: ..." with its source; and, for a leader prepping a rep's call, "[Rep]'s deal. Where [Name] helps: ..." 20 words each |
| `alert` | If the deal is going quiet, the reason in 12 words. Otherwise "" |
| `tiles` | Four: the stage (`n`: the stage name, `label`: "Stage"), the amount (`label`: "Close [date]"), questions to ask (the count, `to: "ask"`), and what's still owed (the count of open commitments, `to: "where"`). Leave a tile out when you can't source it. Never guess a stage |
| `updated`, `built` | When this ran. What you read, and anything that failed or isn't connected, in 40 words or fewer |

**Sections.** Each is `{ id, title, hint, rows, empty }`. A row can use any of these: `lead` (a number in the left margin), `mark` ("good", "bad", "open", or "" for a small colored square when there's no lead), `title` (bold), `meta` (grey, beside the title), `tag` and `tone` (a pill; tone is "good", "bad" or "open"), `text`, `quote` (their exact words), `next` (the one action), `source` ("call, Sep 22", "email, Oct 1", "CRM note"), `steps` (numbered, tucked under "How") and `more` (dated facts, tucked under "Details").

| `id` · `title` | What each row holds | Limits |
|---|---|---|
| `people` · "Attendees" | `title`: the name. `meta`: their job title. `tag`: "new", "skeptic", "champion" or "decides", only when it's earned; `tone` "bad" for skeptic, "good" for champion. `text`: their part in this decision. `source` | text 12 words |
| `where` · "Where we are" | `mark`: "good" for something done, "open" for something still owed by either side, "" for plain history. `tag`: "owed" on open items. `text`: what happened or what's owed, and by whom. `source` | 4 rows; text 12 words. `empty`: "First call. Nothing has happened yet." |
| `care` · "What they care about" | `title`: the point. `quote`: their words. `source` | 3–5 rows; title 8 words |
| `ask` · "Questions to ask" | `mark`: "open". `title`: the question, worded the way the rep would say it. `text`: what it settles and why it matters now | 1–4 rows, the most important first |
| `leave` · "Leave with" | `lead`: "1", "2" and so on. `title`: the thing to walk out with. `text`: why. `steps`: 2–3 steps on how to get it during the call | 2–4 rows; title 8 words |
| `heads` · "Heads up" | `mark`: "bad". `title`: the risk. `next`: how to handle it. `source` | 3 rows |
| `words` · "In their words" | `quote`: the exact phrase. `source` | 3–5 rows |

**Writing the rows.**

- Keep rows to a few words. Anything longer goes in `more`, as dated facts with where each came from.
- Never write "you" or "your" inside `DATA`. Use the person's first name ("Dana owes this"), a rep's first name, or "the team." The page gets forwarded, and "you" means nothing to the next reader. Quotes can keep it, and your chat message can still talk to the person directly.
- Every row that states a fact gets a `source`. The person needs to know what's fact and where to check it.

**What belongs in each section.**

- **Attendees.** Four labels. New: wasn't on earlier calls. Skeptic: pushed back before, so put the quote in `more`. Champion: has sold this internally, so point to the moment. Decides: their title and how they act on calls, never the title alone. Use a label only when you can back it up. A wrong "champion" is worse than no label. If you know nothing about someone, say that, and suggest asking the host who they are.
- **Where we are.** What was decided, what the rep promised and whether it was sent, what the buyer promised and whether it happened.
- **What they care about.** Built up from every touchpoint, in the buyer's own words wherever you have them.
- **Questions to ask.** Real questions the rep can say out loud, in their voice. "Who else needs to sign off before this goes to Rob?" beats "Decision process: unknown."
- **Leave with.** Something they can hold when the call ends: a date, a name, a number, a yes. "Discuss pricing" is a topic and doesn't count. If the buyer asked to see something specific, showing it is usually number one. Tie each to a question, a stage requirement or something the buyer asked for.
- **Heads up.** Only risks with a real source: a competitor that came up, a promise nobody kept, a new stakeholder, a close date that slipped, a long silence.
- **In their words.** From transcripts or emails. If there are no real quotes, leave the section out.

## Step 5: Close

Keep your chat message beside the page short. Four lines at most: (1) the call, and the single most important thing about it; (2) the first-run line, on a first run only; (3) a note on any missing source or skipped meeting; (4) one offer.

- **If you can create scheduled tasks and nothing preps their calls yet:** "Want this ready before every external call? I can run it each weekday at 7am for that day's calls." If they say yes, create a weekday task (7:00 local by default) with the prompt "Run Mutiny meeting prep for each external call on my calendar today", confirm it in one line, and don't offer again. If they say no, leave it there.
- **Otherwise:** "After the call, say 'Run my Mutiny follow-up' and I'll draft the email and the CRM update from here."

## Special cases

- **A first call with nothing from the buyer.** Attendees, Questions to ask and Leave with. The questions are most of discovery. Put "First call" in `sub`.
- **A leader prepping a rep's call** (someone else on their team owns the deal). Add the `notes` line: "[Rep]'s deal. Where [Name] helps: [the gap or decision a leader can unlock, like getting their exec on]." Everything else stays the same.
- **No CRM connected.** Work from calendar, email and calls. Leave the stage and amount tiles out. Don't guess them. Mention once in chat that connecting the CRM or pasting the deal record sharpens the questions.
- **No calendar connected.** Ask for the date, time and attendees in one line, or work from the meeting date and notes they gave you.
- **A source fails.** Try once more, carry on, and say what's missing in `built` and in one line of chat.

## Rules

- **Every fact traces to a source.** The CRM, a call, an email, chat, a contract or the web. If you can't point to where it came from, leave it out. One invented detail and the person starts double-checking everything you write.
- **Leave out empty sections.** Three sections of real content beat seven with filler.
- **Sixty seconds.** They read this right before joining. Keep the rows on show to about 450 words and put the rest in `more`.
- **Facts and prompts. No pep talk.** No "This is a big call!"
- **No emojis.** The template carries the structure.
- **Read only.** Don't update the CRM, send or draft anything, or create a scheduled task unless the person says yes.

## Report template

```html
{{REPORT_TEMPLATE}}
```
