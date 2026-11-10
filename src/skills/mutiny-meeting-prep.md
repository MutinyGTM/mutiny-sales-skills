---
name: mutiny-meeting-prep
description: "Mutiny meeting prep. A 60-second brief for one upcoming call: who you're meeting, what they want to solve, what happened last time and what's still owed, what you still don't know for your qualification method (like the economic buyer), what to push for and what could go sideways. Works for first calls (booking form, intro email) and later ones (every prior call, email and chat). Finds the call on your calendar by itself. For one call, not your whole day. Use whenever someone says 'Run the Mutiny meeting prep for [company]', 'prep me for my call with [company]', 'pre-call prep on [company]', 'what do I need to know before my next call', asks to get ready for a specific sales meeting, or wants prep ready automatically before their meetings. The brief is for the person only; not for writing an agenda or anything to send to the buyer."
---


So they walk into every call ready. This is a brief for one upcoming call that they can read in 60 seconds before they join. It's for the rep. The buyer never sees it.

| Section | What's in it |
|---|---|
| What this call is for | The agenda, and what the buyer wants out of it |
| Who's on the call | Each person's part in the deal, flagged when it's earned (new, skeptic, champion) |
| What they want to solve | Their pain, goals and numbers, in their words |
| Last time and what's owed | What happened before, and what either side still owes |
| Still unknown | The gaps against how this person qualifies |
| What to push for | 2–4 things to leave the call with |
| Watch out for | Real risks, each with a way to handle it |
| Their words | Phrases the buyer uses, worth echoing |

Every section is optional. A first call with no history might have three, and that's the right brief for it.

## Step 1: Find the call

Look at the next 14 days of the calendar for meetings with the company they named, and match each to a CRM deal.

- **One match.** Go straight on. Put the call in the brief's header so a wrong pick is obvious. Don't stop to confirm. Nobody has time for a round trip right before a call.
- **Several meetings on the same deal.** Prep the next one. Mention the later ones in a line at the end.
- **Meetings for different deals or groups at one company** (two business units, say). Ask which, with one line per option: date, time, attendees, deal. This is the only time you ask.
- **No company named.** Prep their next sales call: an external meeting with a buyer, prospect or customer, today or the next working day. You can tell by a CRM deal or contact, or a booking from a prospect. Skip vendors, partners, agencies, recruiting and personal meetings, though a partner or customer who booked through a sales or demo link counts as a sales call. Name what you skipped in a line at the end ("Skipped the 8:00 agency kickoff: not a sales call.").
- **The company they named is a vendor or partner** (they sell to the person, or there's no buyer relationship). Say so under the header and write a short meeting brief: who's coming, what's open on each side, what to get out of it. Leave out the deal and qualification sections.
- **No match.** Say so in two lines with the likely reason (a different name on the invite, a calendar you can't see, not booked yet) and ask for the buyer's name or the meeting details.

## Step 2: Gather

Read widely, then keep only what helps on this call. The reading budget:

- **CRM.** The deal (stage, amount, close date, next step, source, owner, any custom fields that are filled in) and each attendee's contact record. Notes and the last 15 activities. Any form submission that created the contact.
- **Call recordings.** Summaries of every earlier call with this company, however old, and full transcripts of the latest one or two. Prep builds up over time: the first calls usually hold the buyer's original goal, what success means to them and their early doubts, and all of that matters on every call after.
- **Email.** Threads with each attendee from the last 90 days, read to the end. Include replies from teammates the person was copied on and emails the deal owner logged in the CRM. Before you call anything owed, check that nobody on the team already answered it. For a first call, read the thread that booked it closely. Buyers often state their goal or timeline there, and by call time everyone has forgotten.
- **Chat, if it's connected.** Direct messages with attendees, and internal threads about the deal.
- **Contracts, if connected.** Documents that are pending and where each signature stands.
- **Web.** A quick look at any attendee with no CRM or call history: their role and how long they've been there. Company news only when it connects to something the buyer said matters.

Then work out two things. First, the call number: which call this is with the buyer, counting real meetings. Second, whether the buyer has given you anything yet, such as a booking form, a reply to the intro, SDR handoff notes or earlier calls. A first call with a filled-in form isn't a blank slate.

## Step 3: Check it against the profile

This step is the difference between a recap and prep. Use the profile files (see the shared context):

- **Qualification gaps.** Take how they qualify from `mutiny-sales-process.md` under `## Discovery and qualification` (MEDDIC, SPICED, BANT or their own), and the exit criteria for the deal's current stage from `## Pipeline stages`. For each element, decide from the evidence whether it's known, partly known or unknown. The unknowns that matter at this stage go under "Still unknown" ("You still don't know the economic buyer. Only the champion has been on calls."). With no profile, use what any solid discovery checks (budget, decision maker, timeline, the problem, the competition) and say that's what you used.
- **Best-deal moves.** If `mutiny-how-i-work.md` lists moves under `## What I do on my best deals`, suggest the one that fits this call ("On your best deals you get the decision maker on before the pilot starts.").
- **What slips.** Check this deal against each item under `## What slips`, and flag the ones that apply.
- **Competitors.** If one came up, use `mutiny-buyers-and-competitors.md` for how they usually win or lose against it.
- **At risk.** The deal is at risk if there's been no two-way touch in 14 or more days, there's no next step, or a promised next step didn't happen. If so, say it in the header.

## Step 4: Write the brief

The brief is a report page with a fixed design. Copy the template under `## Report template` at the end of this file exactly and replace only the `DATA` object. Don't restyle it, add or remove sections, or write your own HTML. The person should find everything in the same place before every call, scheduled runs included. An empty list shows a short "nothing here" line, and on a first call that's correct.

Show it as an artifact. If you can't, save the filled template as `meeting-prep-[company].html` and share the file. Only when you can't show or save HTML at all, write the same sections in the same order as Markdown (below). The first time someone runs this, add one line in chat: "You'll get the same page before every call. 'How this report works' at the bottom explains each section."

**Filling `DATA`.** Keep rows to a few words. Anything longer goes in `detail`, which is a list of dated facts with their source. Amounts are plain numbers (24000). Never write "you" or "your" inside `DATA`. Use the person's first name ("Dana owes this"), reps' first names, or "the team." The page gets forwarded, and "you" means nothing to the next reader. Quoted text (email subjects, call quotes) can keep it, and your chat message can still talk to the person directly. Every row that states a fact gets a `source` ("call, Sep 22", "email, Oct 1", "CRM note").

| Field | What goes in it | Limit |
|---|---|---|
| `name`, `company`, `updated` | First name; the buyer's company; when this ran | |
| `when`, `callNumber` | "Mon Oct 5 · 4:00pm · 30 min"; "Call 3" or "First call" | |
| `agenda`, `theyWant` | From the invite or booking email; what the buyer asked to cover (with source) | 20 words each |
| `deal` | `stage`, `amount`, `close`, `owner` (first name). Leave a value empty when you can't source it; never guess a stage. No deal means stage "" | |
| `atRisk` | The at-risk reason, if the deal is at risk; else "" | 12 words |
| `note` | Leader prepping a rep's call: "[Rep]'s deal. Where [Name] helps: ..."; vendor or partner meeting: say so; else "" | 25 words |
| `numbers` | `gaps` (items in `unknown`), `owed` (open commitments in `lastTime`) | numbers |
| `want` | `point`, `quote` (their words), `source`, optional `detail` | 3–5 items; point 8 words |
| `watch` | `risk`, `source`, `handle` (how to handle it), optional `detail` | 3 items |
| `push` | `outcome` (something to leave the call with, bold on the page), `why`, `steps` (required: 2–3 numbered steps on how to get it on the call), optional `context` | 2–4 items; outcome 8 words |
| `people` | `name`, `title`, `flag` ("new", "skeptic", "champion", "decision maker" or ""), `role`, `source`, optional `detail` | role 12 words |
| `lastTime` | `text`, `status` ("done", "open" for a commitment still owed, or ""), `source`, optional `detail` | 4 items; 12 words |
| `unknown` | `item` (an element of how they qualify), `why` (why it matters at this stage, phrased so it turns into a question) | 1–4 items |
| `words` | `phrase` (exact), `source` | 3–5 items |
| `howBuilt` | What was read, anything that failed or isn't connected | 40 words |

Markdown version, only when HTML isn't possible:

```
**Meeting prep: [Company]** · [Day] [time] · [length] · call [N]
[Deal name] · [stage] · $[amount] · close [date][ · at risk: reason]

**What this call is for**
- Agenda: [from the invite or booking email]
- They want: [what the buyer asked to cover, with source]

**Who's on the call**
- **[Name], [title]**: [their part in the deal, what they care about]. [Flag]
- **[Name], [title]**: [role]. New to the deal; [LinkedIn link]

**What they want to solve**
- [Pain or goal]: "[their words]" ([source, date])

**Last time and what's owed**
- [What happened or was decided] ([source, date])
- You promised [deliverable] by [date]: [sent / not sent yet]
- They promised [thing]: [done / still open]

**Still unknown**
- [Element of how they qualify]: [what's missing and why it matters at this stage]

**What to push for**
1. [Specific outcome]: [why, and what you need to hear]

**Watch out for**
- [Risk] ([where it came from]) → [how to handle it]

**Their words**
- "[exact phrase]" ([source])
```


Notes on each section:

- **Sources.** End every bullet under Who's on the call, What they want to solve, Last time and Their words with a short source tag ("(call, Sep 22)", "(email, Oct 1)", "(CRM note)"). The person needs to know what's fact and where to check it.
- **Who's on the call.** Four flags. New: wasn't on earlier calls. Skeptic: pushed back before, so give the quote. Champion: has sold this internally, so point to the moment. Decision maker: the title and how they act on calls, never the title alone. Use a flag only when you can back it up. A wrong "champion" label is worse than no label. If you know nothing about someone, say that, and suggest asking the host who they are.
- **What they want to solve.** 3–5 bullets, built up from every touchpoint, in the buyer's own words wherever you have them.
- **Still unknown.** 1–4 items, with the one that matters most at this stage first. Phrase each so it becomes a question on the call.
- **What to push for.** Things to leave the call with: a date, a name, a number, a yes. Topics ("discuss pricing") and approaches ("reframe around the new product") don't count. If the buyer asked to see something specific, showing it is usually number one. Tie each to a gap, a stage requirement or something the buyer asked for.
- **Watch out for.** Only risks with a real source: a competitor that came up, a promise nobody kept, a new stakeholder, a close date that slipped, a long silence.
- **Their words.** 3–5 phrases from transcripts or emails. If there are no real quotes, skip the section.

## Step 5: Close

Keep your chat message beside the page short. Four lines at most: (1) the call, and the single most important thing about it; (2) the first-run line, on a first run only; (3) a note on any missing source or skipped meeting; (4) one offer.

- **If you can create scheduled tasks and nothing preps their calls yet:** "Want this ready before every external call? I can run it each weekday at 7am for that day's calls." If they say yes, create a weekday task (7:00 local by default) with the prompt "Run Mutiny meeting prep for each external call on my calendar today", confirm it in one line, and don't offer again. If they say no, leave it there.
- **Otherwise:** "After the call, say 'Run my Mutiny follow-up' and I'll draft the follow-up and CRM note from this context."

## Special cases

- **A first call with nothing from the buyer.** Header, Who's on the call, What to push for, and Still unknown, which is most of discovery. Say "First call, no prior touchpoints."
- **A leader prepping a rep's call** (someone else on their team owns the deal). Add one line under the header: "[Rep]'s deal. Where [Name] helps: [the gap or decision a leader can unlock, like getting the exec on]." Everything else stays the same.
- **No CRM connected.** Work from calendar, email and calls. Mark stage and amount unknown. Don't guess them. Mention once at the end that connecting the CRM or pasting the deal record sharpens the gaps.
- **No calendar connected.** Ask for the date, time and attendees in one line, or work from the meeting date and notes they gave you.
- **A source fails.** Try once more, carry on, and say in one line what's missing.

## Rules

- **Every fact traces to a source.** The CRM, a call, an email, chat, a contract or the web. If you can't point to where it came from, leave it out. One invented detail and the person starts double-checking everything you write.
- **Drop empty sections.** Three sections of real content beat eight with filler.
- **Sixty seconds.** They read this right before joining. Keep the visible rows to about 450 words and put the rest in `detail`.
- **Facts and prompts. No pep talk.** No "This is a big call!"
- **No emojis.** The template carries the structure. In the Markdown version, bold labels do.
- **Read only.** Don't update the CRM, send or draft anything, or create a scheduled task unless the person says yes.

## Report template

```html
{{REPORT_TEMPLATE}}
```
