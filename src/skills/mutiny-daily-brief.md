---
name: mutiny-daily-brief
description: "Mutiny daily brief, from Sales Skills by Mutiny. The rep's day, sorted before they log on: one page they can read on a phone that says where to start, what moved while they were out, who they're meeting and where each deal stands, which buyers are waiting on them, and which deals are going quiet. Sales leaders also see a line for each rep. Built from the calendar, CRM, call recordings, email and chat, and shaped by the person's sales profile. Read only. Use whenever someone says 'Run my Mutiny daily brief', asks what's on today, what they missed overnight, what needs them this morning, or wants a rundown of their day and pipeline, even if they never say the word 'brief'."
---


Their day, sorted before they log on. One page, short enough to read on a phone over coffee, ahead of the first call.

| Section | What it tells them |
|---|---|
| Start here | The 2–5 things that matter most today, in order |
| While you were out | Buyer replies, stage changes, wins, losses and signed contracts since yesterday |
| Today's meetings | Each sales call: who's on it, where the deal stands, what's still open |
| Waiting on you | Buyers who wrote last and haven't heard back |
| Going quiet | Deals that are stalling or slipping |
| Your team (leaders) | A line per rep: what's stalling, what's closing, where the leader is needed |
| Open time | Free blocks of 30 minutes or more |

## Step 1: Read the profile

The profile files (see the shared context) tell you what matters to this person. Use them to decide what goes on the page:

- `mutiny-how-i-work.md`: `## What slips` is the person's own watch list, so check today's calls and deals against each item. `## Where my time goes` tells you which prep to do for them. `## My rules` apply to every action you suggest.
- `mutiny-sales-process.md`: the stage names, what has to be true to move on, and how they qualify under `## Discovery and qualification`. These tell you whether a deal is stuck.
- `mutiny-buyers-and-competitors.md`: the competitor names, so you recognize one when it comes up.
- `mutiny-how-we-work.md`, or a leader role under `## About me`: switch on the Your team section.

If there's no profile, or it doesn't say whether they lead a team, work it out. They do if other people own most of the deals they're involved in (as a contact, a follower or a meeting attendee), or their calendar has recurring 1:1s with reps. If so, switch on Your team.

With no profile at all, run the brief anyway and use the CRM's stage names.

## Step 2: Gather

Read everything before you write a word. Hold to this budget so the brief comes back fast:

- **Calendar.** Every meeting today. Sort them into three piles: sales calls (with a buyer, prospect or customer, which you can tell from a CRM deal or contact, or a booking from a prospect), other external meetings (vendors, partners, agencies, recruiting), and internal ones. Note every open block of 30 minutes or more.
- **Each sales call.** The matching CRM deal (stage, amount, close date, next step), its last 3–5 activities, the most recent call summary, and the latest email or chat thread with the people attending. Look for what was promised and whether it happened. If the CRM is thin on a new contact, a quick web search for their role is enough. Deeper research is meeting prep's job.
- **Since yesterday.** Everything since the start of the previous working day. On a Monday, that's Friday morning. Buyer emails and chat messages that came in. Stage changes. Deals created, won or lost. Contracts signed or viewed. Use CRM activity or stage history where there is any. Where there isn't, compare last-modified dates and say the stage change is inferred.
- **Waiting on you.** Buyer or prospect emails and direct messages from the last 7 days where the buyer wrote last and the person hasn't answered. Skip newsletters, automated mail, internal threads and group channels. Skip replies to a mass email (a webinar, a newsletter) unless they ask the person something.
- **Pipeline.** The open deals the person owns, or their team's for a leader. Up to 150, through filtered queries. Don't read each record. Read notes only on deals that look like they're stalling. If there are more than 150, say how many you read.

**When a deal counts as going quiet.** Any one of three things puts it at risk: no two-way touch (a buyer reply, a call, a meeting) in 14 or more days; no next step on the deal; or a promised next step that didn't happen (a date that passed, something that was never sent, a meeting that never got booked). A few details:

- Check email, chat and call history before you call a deal quiet. If the buyer replied in chat yesterday, it isn't quiet, whatever the CRM says.
- A close date that has passed makes a deal "slipped." That alone doesn't put it on the list. Mention it when the deal is there for another reason.
- A contract that's been unsigned for 7 or more days counts as a promised next step that didn't happen.
- Deals with no activity in 60 or more days, often sitting in an old pipeline, get named in the section's `foot` as ones to close out. They don't get rows. This list is for deals that can still be saved.
- A deal created in the last 14 days isn't at risk just because it has no next step yet. That's normal for a new deal.

## Step 3: Build the page

The brief is a page with a fixed design. Copy the template under `## Report template` at the end of this file exactly and replace only the `DATA` object. Don't restyle it or write your own HTML. Use the sections below, in this order, every time, so the person finds everything where it was yesterday. A section with nothing in it stays on the page with its `empty` line.

Show the page as an artifact. If you can't, save the filled template as `daily-brief.html` and share the file. Only when you can't show or save HTML at all, write it as Markdown: the same sections in the same order, each title as a `##` header and each row as one bullet. The first time someone runs this, add one line in chat: "You'll get this same page every morning. 'How this page works' at the bottom explains each section."

**Top of `DATA`:**

| Field | What goes in it |
|---|---|
| `kind` | "Daily brief" |
| `title` | "Good morning, [first name]." For a leader with a team section, "[Company] sales, [weekday]" |
| `sub` | The date and the view: "Tuesday, October 6 · My day" or "Tuesday, October 6 · My day and 3 reps" |
| `tiles` | Four, in this order: sales calls today (`to: "meetings"`), buyers waiting (`to: "waiting"`), deals going quiet, as the full count (`to: "quiet"`), and new since yesterday (`to: "news"`). Each is `{ n, label, to }` |
| `updated`, `built` | When this ran. What you read, any sampling, and anything that failed or isn't connected, in 40 words or fewer |

**Sections.** Each is `{ id, title, hint, rows, empty, foot }`. A row can use any of these: `lead` (a number or a time in the left margin), `mark` ("good", "bad", "open", or "" for a small colored square when there's no lead), `title` (bold), `meta` (grey, beside the title), `tag` and `tone` (a pill; tone is "good", "bad" or "open"), `lines` (short grey lines), `text`, `next` (the one action), `source`, `steps` (numbered, tucked under "How") and `more` (dated facts with their source, tucked under "Details").

| `id` · `title` | What each row holds | Limits |
|---|---|---|
| `first` · "Start here" | `lead`: "1", "2" and so on. `title`: the company. `meta`: the amount, and for a leader whose deal it is. `text`: the action, starting with a verb and naming who to contact ("Email Dana to book the security review"). `source`: why today. `steps`: 2–3 steps, each with who, how and by when | 2–5 rows; text 8 words; source 12 words. `empty`: "Nothing urgent. Just show up to your calls." |
| `news` · "While you were out" | `mark`: "good" for moved forward, won or signed; "bad" for lost or slipped; "" for a reply or neutral news. `title`: the company. `meta`: amount, owner. `text`: what changed. `more`: the dated facts | 6 rows; text 10 words |
| `meetings` · "Today's meetings" | `lead`: the time. `title`: the company. `meta`: the kind of call. `lines`: the people ("Name (title) · Name (title)"), then the deal ("Pricing · $24k · close Nov 16 · last heard from them 6 days ago"). `text`: what happened last time and what's still open. `next`: one thing to do before the call, if there is one. `more`: dated facts | Sales calls only; text 25 words. `foot`: one line for every other meeting ("Also: 8:00 agency kickoff, 3 internal") |
| `waiting` · "Waiting on you" | `mark` and `tone`: "bad" at 2 or more days, otherwise "open". `title`: the person. `meta`: company and channel. `tag`: "3d waiting" or "today". `text`: what they asked | 5 rows |
| `quiet` · "Going quiet" | `mark`: "bad". `title`: the company. `meta`: amount, stage, owner. `tag`: "16d quiet · email", or "no touch logged"; `tone` "bad" at 14 days or more. `text`: which of the three reasons, with the date. `next`: one action. `more`: dated facts | Worst first. Up to 5 rows, or 6 for a leader. `foot`: how many more there are, by name or by rep, then "Close out (no activity in 60+ days): [names]" |
| `team` · "Your team" | Leaders only; leave the whole section out otherwise. `mark`: "bad" if the rep has deals going quiet, else "good". `title`: the rep's first name. `meta`: "2 closing this week". `tag`: "3 going quiet" or "On track". `text`: the one deal or decision that needs the leader. `more`: that rep's quiet deals, one line each | One row per rep, most at risk first; text 15 words |
| `open` · "Open time" | `title`: "3:00–4:00". `meta`: "1 hr" | Blocks of 30+ minutes. `empty`: "No open blocks of 30 minutes or more." |

**Writing the rows.**

- Keep rows to a few words. The full story goes in `more`, as dated facts with where each came from ("Sep 30 call: asked for the security doc").
- Amounts go in as short money ("$24k"). Leave them out when they're zero or unknown.
- Use first names for people and company names for deals. Never the CRM's deal name.
- Never write "you" or "your" inside `DATA`. Use the person's first name ("Dana owes this"), a rep's first name, or "the team." The page gets forwarded, and "you" means nothing to the next reader. Quoted text can keep it, and your chat message can still talk to the person directly.

**What belongs in each section.**

- **Start here.** Pull the most important items from every other section and rank them by what's due soonest. Anything blocking a call today goes first. Make each one concrete ("Send the security doc to [Buyer] before the 2pm call"). "Follow up with [Company]" is too general to act on. Let `## What slips` from the profile decide what rises to the top.
- **Today's meetings.** Mark a first call. Mark anyone new to the deal and give their LinkedIn link in `more`, because that's the one time the link earns its space. If the deal is missing something obvious for its stage by their own way of qualifying (a pilot with nobody named who signs off, say), put it in `text`.
- **Going quiet.** Every row names the specific reason and one action.
- **Your team.** Give the counts, then the single deal or decision that most needs the leader: a close this week going quiet, an approval, an exec intro, a call they're joining. The full list comes from a Mutiny check-in pipeline scan. It doesn't belong here. The leader's own deals stay in the sections above.
- **Open time.** List the blocks and stop. Don't plan their time for them.
- **Length.** The rows on show should take a minute to read: about 400 words, or 500 for a leader. Everything else goes in `more`. Keep to the row limits and sum up what's left over in the section's `foot` ("+4 stage moves on the team").

## Step 4: Close

Keep your chat message beside the page short. Four lines at most: (1) what's most urgent; (2) the first-run line, on a first run only; (3) one offer, which is the scheduling offer if it applies, otherwise the next skill, or the setup suggestion when there's no profile; (4) a note on any missing source.

1. **One next skill, and only if it's earned.** "Want me to run meeting prep on the [time] [Company] call?" Or "The [Company] call yesterday has no follow-up yet. Want me to draft the follow-up?" Or "Want me to draft a check-in for [Company]?" On a clean day, skip it.
2. **Scheduling, only if you can create scheduled tasks and none already runs the daily brief.** "Want this waiting for you every weekday at 7am? Say yes, or give me a time." Check the existing scheduled tasks first. If they say yes, create a weekday task (7:00 local by default) with the prompt "Run my Mutiny daily brief", confirm it in one line, and don't offer again. If you can't create scheduled tasks, say nothing about scheduling.

## Special cases

- **No calendar connected.** Use a pasted calendar if they gave you one. If not, leave Today's meetings and Open time with their `empty` lines and add one line in chat: "Connect your calendar (your name at the bottom left, then Settings, then Connectors) and I'll include today's meetings."
- **No CRM connected.** Use pasted deals if they gave you any. If not, build the meetings and the pipeline view from email, calls and calendar, mark the stages as inferred, and mention once that connecting the CRM or pasting a CSV export of open deals makes the Going quiet list complete.
- **A source fails partway.** Try once more, then carry on with what you have and say so in `built` and in one line of chat ("Email didn't load, so Waiting on you may be incomplete").
- **No calls today.** That's still a brief worth reading: Start here, While you were out and Going quiet carry it.
- **A weekend or a holiday.** Brief the next working day and say so in `sub`.
- **A leader with no deals of their own.** If they have no external meetings, Your team is the section that matters. Move it up to sit right after While you were out.

## Rules

- **Only what you verified.** If there's no data on a call, write "No history found." Don't guess what the call is about. One wrong fact in a page they read every morning teaches them to stop reading it.
- **Specific over general.** Quote the commitment and the date ("Dana said she'd send the case study by Friday. Not sent yet."). A vague flag gets skipped.
- **No cheerleading, no padding.** This is a memo. A suggested action is fine. "Big day!" isn't.
- **Background research only when it changes the call.** Company news, funding or LinkedIn posts go in only when they tie to something in the deal. Competitors go in only when they came up in a real conversation.
- **No emojis.** The template carries the structure.
- **Read only.** Don't update the CRM, send anything, draft into their inbox or create anything unless the person approves it. The scheduled task gets created only after they say yes.

## Report template

```html
{{REPORT_TEMPLATE}}
```
