---
name: mutiny-daily-brief
description: "Mutiny daily brief. A short read for the start of the day, built for a phone: what to do first, what changed since yesterday (new replies, stage changes), today's calls with deal context, messages waiting on a reply, deals at risk, and open time. Sales leaders also get a line per rep. Pulls calendar, CRM, call recordings, email and chat, and uses the person's sales profile. Use whenever someone says 'Run my Mutiny daily brief', asks what's on today, what they missed overnight, what needs them this morning, or wants a rundown of their day and pipeline, even if they don't say 'brief'."
---


Their day, sorted before they log on. One page, short enough to read on a phone over coffee, ahead of the first call.

| Section | What's in it |
|---|---|
| Do first | The 2–5 things that matter most today, in order |
| Since yesterday | Buyer replies, stage changes, wins, losses, signed contracts |
| Today's calls | Each external call: who's on it, where the deal stands, what's open |
| Replies waiting | Buyers who are waiting to hear back from the person |
| At risk | Deals going quiet or slipping |
| Team (leaders) | One line per rep: what's at risk, what's closing, what needs the leader |
| Open time | Free blocks of 30 minutes or more |

## Step 1: Read the profile

The profile files (see the shared context) tell you what matters to this person. Use them to decide what goes on the page:

- `mutiny-how-i-work.md`: `## What slips` is the person's own watch list, so check today's calls and deals against each item. `## Where my time goes` tells you which prep to do for them. `## My rules` apply to every action you suggest.
- `mutiny-sales-process.md`: the stage names, what has to be true to move on, and how they qualify under `## Discovery and qualification`. These tell you whether a deal is stuck.
- `mutiny-buyers-and-competitors.md`: the competitor names, so you recognize one when it comes up.
- `mutiny-how-we-work.md`, or a leader role under `## About me`: switch on the Team section (Step 3).

If there's no profile, or it doesn't say whether they lead a team, work it out. They do if other people own most of the deals they're involved in (as a contact, a follower or a meeting attendee), or their calendar has recurring 1:1s with reps. If so, switch on Team.

With no profile at all, run the brief anyway and use the CRM's stage names.

## Step 2: Gather

Read everything before you write a word. Hold to this budget so the brief comes back fast:

- **Calendar.** Every meeting today. Sort them into three piles: sales calls (with a buyer, prospect or customer, which you can tell from a CRM deal or contact, or a booking from a prospect), other external meetings (vendors, partners, agencies, recruiting), and internal ones. Note every open block of 30 minutes or more.
- **Each sales call.** The matching CRM deal (stage, amount, close date, next step), its last 3–5 activities, the most recent call summary, and the latest email or chat thread with the people attending. Look for what was promised and whether it happened. If the CRM is thin on a new contact, a quick web search for their role is enough. Deeper research is meeting prep's job.
- **Since yesterday.** Everything since the start of the previous working day. On a Monday, that's Friday morning. Buyer emails and chat messages that came in. Stage changes. Deals created, won or lost. Contracts signed or viewed. Use CRM activity or stage history where there is any. Where there isn't, compare last-modified dates and say the stage change is inferred.
- **Replies waiting.** Buyer or prospect emails and direct messages from the last 7 days where the buyer wrote last and the person hasn't answered. Skip newsletters, automated mail, internal threads and group channels. Skip replies to a mass email (a webinar, a newsletter) unless they ask the person something.
- **Pipeline.** The open deals the person owns, or their team's for a leader. Up to 150, through filtered queries. Don't read each record. Read notes only on deals that look at risk. If there are more than 150, say how many you read.

**At risk** means any one of three things: no two-way touch (a buyer reply, a call, a meeting) in 14 or more days; no next step on the deal; or a promised next step that didn't happen (a date that passed, something that was never sent, a meeting that never got booked). A few details:

- Check email, chat and call history before you call a deal quiet. If the buyer replied in chat yesterday, it isn't quiet, whatever the CRM says.
- A close date that has passed makes a deal "slipped." That alone doesn't make it at risk. Mention it in the deal's `why` when the deal is at risk for another reason.
- A contract that's been unsigned for 7 or more days counts as a promised next step that didn't happen.
- Deals with no activity in 60 or more days, often sitting in an old pipeline, go in `closeOut` by name and stay out of `atRisk`. The at-risk list is for deals that can still be saved.
- A deal created in the last 14 days isn't at risk just because it has no next step yet. That's normal for a new deal.

## Step 3: Write the brief

The brief is a report page with a fixed design. Copy the template under `## Report template` at the end of this file exactly and replace only the `DATA` object. Don't restyle it, add or remove sections, or write your own HTML. The person should find everything in the same place every morning, scheduled runs included. An empty list shows a short "nothing here" line, and on a quiet day that's correct.

Show it as an artifact. If you can't, save the filled template as `daily-brief.html` and share the file. Only when you can't show or save HTML at all, write the same sections in the same order as Markdown (below). The first time someone runs this, add one line in chat: "You'll get the same page every morning. 'How this report works' at the bottom explains each section."

**Filling `DATA`.** Keep rows to a few words. The full story goes in `detail`, which is a list of dated facts with their source ("Sep 30 call: asked for the security doc"). Amounts are plain numbers (24000), and you leave them out when they're 0 or unknown. Use first names for people, in `owner` too. Use company names, never CRM deal names. Never write "you" or "your" inside `DATA`. Use the person's first name ("Dana owes this"), reps' first names, or "the team." The page gets forwarded, and "you" means nothing to the next reader. Quoted text (email subjects, call quotes) can keep it, and your chat message can still talk to the person directly.

| Field | What goes in it | Limit |
|---|---|---|
| `name`, `company`, `date`, `view`, `updated` | First name; their company (from the profile, CRM or email domain; titles the page when there's a Team section, "Sales team" if unknown); "Tuesday, October 6"; "My day" or "My day + team · 3 reps"; when this ran | |
| `numbers` | `calls` (sales calls today), `replies`, `atRisk` (the full count, even if fewer are listed), `changes` (items in New since yesterday) | numbers |
| `doFirst` | `deal` (the company, shown in bold so the eye finds the account first), `amount`, `owner` (leaders: whose deal), `action` (starts with a verb and names who to contact, "Email Dana to book the security review"), `why`, `steps` (required: 2–3 numbered steps, who, how, by when), optional `context` (date and source) | 2–5 items; action 8 words, why 12 |
| `sinceYesterday` | `kind` ("good": moved forward, won, signed; "bad": lost, slipped; "" for a reply or neutral news), `deal`, optional `amount` and `owner`, `what`, `detail` | 6 items; what 10 words |
| `atRisk` | Every at-risk deal, worst first (up to about 40; the page shows the top 5, or the 6 biggest team-wide for leaders, and groups the rest by rep): `deal`, `amount`, `owner`, `stage`, `quietDays` (number, or null if no touch is logged), `channel` of the last touch, `why` (which at-risk reason), `next` (one action), `detail` | why 12 words |
| `calls` | `time`, `company`, `type`, `people` ("Name (title) · Name (title)"), `deal` ("Stage · $24k · close Nov 16 · last two-way touch 6 days ago"), `open` (what happened last time and what's still open), optional `prep` (one action), `detail` | sales calls only; open 25 words |
| `otherMeetings` | One line for vendor, partner and internal meetings | 15 words |
| `closeOut` | Names of deals with no activity in 60+ days, shown as one line | names only |
| `replies` | `name`, `company`, `channel`, `ask`, `waitingDays` (number), `detail` | 5 items |
| `team` | Leaders only, one per rep, most at risk first: `name` (exactly as in `owner`, since opening a rep lists their at-risk deals), `atRiskCount`, `closingCount` (this week), `ask` (the one thing that needs the leader), optional `detail` | ask 15 words |
| `openTime` | `start`, `end`, `length` for blocks of 30+ minutes | |
| `howBuilt` | What was read, any sampling, anything that failed or isn't connected | 40 words |

Markdown version, only when HTML isn't possible:

```
**Daily brief · [Weekday], [Month] [Day]**
[N] calls · [N] replies waiting · [N] at risk

**Do first**
1. [Specific action] — [why today, one line]
2. [Specific action] — [why today]

**Since yesterday**
- [Company]: [Buyer] replied — [what they said or asked, a few words]
- [Company]: moved [stage] → [stage]
- [Company]: [won / lost / contract signed]

**Today's calls**
**[Time] · [Company]** · [call type]
[Name] ([title]) · [Name] ([title])
[Stage] · $[amount] · close [date] · last two-way touch [N] days ago
[One or two lines: what happened last time and what's still open.]
→ [One action before the call, if there is one]

**Replies waiting**
- [Name], [Company] · [email / chat] · [what they asked] · [N] days

**At risk**
- [Company] · [stage] · $[amount] · [the reason: quiet [N] days / no next step / promised [X] by [date], not done] → [action]

**Team**
- [Rep]: [N] at risk, [N] closing this week. [The one deal or decision that needs the leader.]

**Open time**
[Start]–[End] · [Start]–[End]
```


Notes on each section:

- **Do first.** Pull the most important items from every other section and rank them by what's due soonest. Anything blocking a call today goes first. Make each one concrete ("Send the security doc to [Buyer] before the 2pm call"). "Follow up with [Company]" is too general to act on. Let `## What slips` from the profile decide what rises to the top. On a clean day, write "Nothing urgent. Just show up to your calls."
- **Today's calls.** Sales calls only, five lines each at most. Mark a first call. Mark anyone new to the deal and give their LinkedIn link, because that's the one time the link earns its space. If the deal is missing something obvious for its stage by their own way of qualifying (a pilot with no economic buyer named, say), put it in the "still open" line. Vendor, partner and internal meetings share one line at the end ("Also: 8:00 agency kickoff, 3 internal"). Flag one only if something is due before it.
- **At risk.** Put every at-risk deal in `DATA`, worst first. The page shows the top few and sums up the rest. Every line names the specific reason and one action.
- **Team (leaders only).** One line per rep, under 30 words, worst first. Give the counts, then the single deal or decision that most needs the leader: a close this week going quiet, an approval, an exec intro, a call they're joining. The full list comes from a Mutiny check-in pipeline scan. It doesn't belong here. The leader's own deals stay in the sections above.
- **Open time.** List the blocks and stop. Don't plan their time for them.
- **Length.** The visible rows should take a minute to read: about 400 words, or 500 for a leader. Everything else goes in `detail`. Keep to the item limits and group what's left over ("+4 stage moves on the team"). In the Markdown version, if they say they're on their phone or in a hurry, stay under 300 words: Do first and Since yesterday in full, then only what needs action today.

## Step 4: Close

Keep your chat message beside the page short. Four lines at most: (1) what's most urgent; (2) the first-run line, on a first run only; (3) one offer, which is the scheduling offer if it applies, otherwise the next skill, or the setup suggestion when there's no profile; (4) a note on any missing source.

1. **One next skill, and only if it's earned.** "Want me to run meeting prep on the [time] [Company] call?" Or "The [Company] call yesterday has no follow-up yet. Want me to draft the follow-up?" Or "Want me to draft a check-in for [Company]?" On a clean day, skip it.
2. **Scheduling, only if you can create scheduled tasks and none already runs the daily brief.** "Want this waiting for you every weekday at 7am? Say yes, or give me a time." Check the existing scheduled tasks first. If they say yes, create a weekday task (7:00 local by default) with the prompt "Run my Mutiny daily brief", confirm it in one line, and don't offer again. If you can't create scheduled tasks, say nothing about scheduling.

## Special cases

- **No calendar connected.** Use a pasted calendar if they gave you one. If not, skip Today's calls and Open time and add one line at the end: "Connect your calendar (your name at the bottom left, then Settings, then Connectors) and I'll include today's calls."
- **No CRM connected.** Use pasted deals if they gave you any. If not, build the calls and the pipeline view from email, calls and calendar, mark the stages as inferred, and mention once at the end that connecting the CRM or pasting a CSV export of open deals makes the at-risk list complete.
- **A source fails partway.** Try once more, then carry on with what you have and say so in one line at the end ("Email didn't load, so Replies waiting may be incomplete").
- **No calls today.** Lead with Do first, then Since yesterday and At risk. That's still a brief worth reading.
- **A weekend or a holiday.** Brief the next working day and say so in the header.
- **A leader with no deals of their own.** Skip Today's calls if they have no external meetings. Team becomes the main section, right after Since yesterday.

## Rules

- **Only what you verified.** If there's no data on a call, write "No history found." Don't guess what the call is about. One wrong fact in a page they read every morning teaches them to stop reading it.
- **Specific over general.** Quote the commitment and the date ("You said you'd send the case study by Friday. Not sent yet."). A vague flag gets skipped.
- **No cheerleading, no padding.** This is a memo. A suggested action after → is fine. "Big day!" isn't.
- **Background research only when it changes the call.** Company news, funding or LinkedIn posts go in only when they tie to something in the deal. Competitors go in only when they came up in a real conversation.
- **No emojis.** The template carries the structure. In the Markdown version, bold labels do.
- **Read only.** Don't update the CRM, send anything, draft into their inbox or create anything unless the person approves it. The scheduled task gets created only after they say yes.

## Report template

```html
{{REPORT_TEMPLATE}}
```
