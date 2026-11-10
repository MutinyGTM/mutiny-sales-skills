---
name: mutiny-setup
description: "Mutiny setup, from Sales Skills by Mutiny. Run this first. It learns how the person writes and sells from their own CRM, call recordings, email and calendar, then saves a short sales profile that every other Sales Skill reads, so follow-ups, check-ins and customer pages sound like them and not like AI. The profile covers their voice with real examples, how their deals move and how they qualify, who they sell to, pricing, competitors, brand and customer proof, and their own habits and rules. Sales leaders also get team files to hand to their reps. It takes 5 to 10 minutes and two short replies, and it only reads. Use whenever someone says 'Build my sales profile', 'Refresh my sales profile' or 'Set up Sales Skills by Mutiny', wants Claude set up for selling, wants Claude to learn their voice or how their team sells, or wants drafts that sound like them."
---


This is where you learn to sound like the person. Everything the other Sales Skills draft, from a follow-up to a pricing proposal, is only as good as what you save here.

You're building four short files from their real emails, calls and deals. Sales leaders get a fifth.

| File | What it holds | Whose it is |
|---|---|---|
| `mutiny-voice.md` | How they write and talk: tone, greeting and sign-off, structure, the phrases that are theirs, what gets replies, and a real example for each situation (first follow-up, post-demo recap, check-in, pricing, scheduling) | Theirs |
| `mutiny-sales-process.md` | Why they win and lose, each stage and what it takes to leave it, how they qualify, the basic numbers | The team's |
| `mutiny-buyers-and-competitors.md` | What they sell, who buys it, pricing, a line or two on each competitor, their brand basics and customer proof | The team's |
| `mutiny-how-i-work.md` | What they do on their best deals, where their hours go, what slips, their rules, their tools | Theirs |
| `mutiny-how-we-work.md` (leaders only) | The team, the handoffs, what every rep does on every deal, what the leader wants to see each week | The team's |

Each skill reads what it needs. Follow-ups and check-ins lean on voice. Meeting prep leans on process. Pricing proposals, business cases and deal rooms lean on buyers, pricing, brand and proof. When a rep adds their leader's team files, the whole team runs one process and every rep still sounds like themselves.

You get two replies from the person: one to point you at a killer deal, one to confirm what you found. Their data answers everything else.

## Show what you read

No progress bars, step counters or status lines on any setup message. Just say what you're doing in plain words.

When you've finished reading, show what you read in one small table, with a real count on every row:

```
| Source | What I read |
|---|---|
| CRM | 46 open deals, 112 closed in the last 6 months |
| Calls | Your last 10 calls |
| Email | 28 emails you sent to buyers, and their replies |
| Calendar | Not connected, so no meeting context |
```

## Step 1: Ask for one killer deal

Ask one thing before you read anything. Anyone can answer it, and the answer shows you what good looks like for this person:

```
I'm about to read your CRM, calls and email so that what I draft sounds like you, not like AI. Give me a few minutes. First:

**What's one killer deal you could point me to?**

Yours or your team's, won or lost, big or small. The one that was run the way you'd run every deal if you had the time.
Or say "skip" and I'll find your best win myself.
```

If they asked for less (say, "learn how I write"), tell them in a line that voice is one of four short files and the other three cost them nothing extra. Then carry on.

If the project already holds `mutiny-*.md` team files, say so now ("I can see your team's process files, so I'll spend my time on your voice and how you work.") and follow "Team files already in the project" under Special cases.

## Step 2: Read everything

Find out what's connected by trying it: CRM, call recorder, email, calendar, then chat and documents. Only name a source once it has answered. Go back six months, or as far as the reading budget lets you. The budget wins. Stretch to twelve months only when the data is thin.

**Reading budget.** Hold to it, so setup finishes in one chat:
- **CRM:** filtered queries and totals. Don't open records one by one. No more than 200 deal records. Read notes only on the best deals, 10 recent wins and 10 recent losses, and skip any note that's a long paste (a Slack thread, a log).
- **Calls:** use the summaries that come back in a list (often 20 at a time). Pull full transcripts for 3 at most, starting with calls from the best deals.
- **Email:** up to 25 threads they sent. Read only as much of each as you need.
- **Best deals:** the full history for 2 at most: the killer deal they named, and one more win you pick yourself.
- **Leaders:** totals per rep (deal count, conversion, time in stage), and the full notes on one deal per rep.

When a source is bigger than the budget, read the most recent slice and say so ("read 200 of about 1,400 deals").

**Scope.** For a rep, only the deals they own. For a leader, only their team's deals: use team or role data, or the owners of deals the leader has touched in the last 90 days. Never hand someone the whole company's numbers as their own. If company-wide is all you can see, label it "company-wide."

A source that's missing, broken or thin doesn't stop setup. Special cases, at the end, covers each one.

### CRM: the process

Pull the open deals (stage, amount, close date, age in stage, last activity, owner), the deals won and lost in the last six months, the stage names for every pipeline, contact titles and company types, amounts and products, and notes. You're looking for five things:

- **How they really sell.** Where leads come from, what the first call covers, when pricing comes up, who gets brought in, what tips a deal to closed.
- **Stages.** Conversion from one to the next and the usual time in each. If the CRM has no stage-entry dates, use created-to-closed time and say that's what you did. Then work out from notes, calls and email what actually happens before a deal moves. Those are the exit criteria.
- **How they qualify.** MEDDIC, MEDDPICC, SPICED, BANT or something of their own, read from the fields, the notes and how they talk on calls. Note what always gets captured and what usually doesn't.
- **Won against lost.** What the wins had that the losses didn't (more than one contact, a champion, a recap after the demo, a business case before pricing), and where the losses died.
- **Numbers.** Deal size, cycle length, and win rate if you can see it.

### Calls: how they sell, out loud

Read the recent summaries and three full transcripts, best-deal calls first. Listen for how they open, what they ask in discovery, how they describe the product, how they handle price and pushback, which competitors come up and what they say about them, how they build rapport, how they handle a tense moment, and how they end a call and set the next step. Keep their exact words.

### Email: the voice

Read up to 25 threads they sent to buyers, with the buyers' replies. Set aside anything they didn't type themselves: internal mail, newsletters, sequence or template emails (the same text sent to many people, often with a different signature), and any signature or footer their email tool adds. Write down how their signature gets added, so drafts never type a second one.

- **Mechanics.** The exact greeting and sign-off. Sentence and paragraph length. Bullets or prose. How formal, how funny. Exclamation marks, emoji, subject lines.
- **Structure.** Whether the ask comes first or last, how they close, how many asks they make in one email.
- **By situation.** Sort the emails into first follow-up, post-demo recap, check-in on a quiet deal, pricing or proposal, scheduling, and quick reply. Notice how the tone changes between them, and keep one or two real examples of each.
- **Phrases that are theirs.** Five to eight lines, word for word.
- **What gets replies.** Set the emails that got an answer beside the ones that didn't, and compare length, subject line, and whether they ended on a question. Report a pattern only when there are enough examples to trust it.
- **Rules they follow.** What they always or never do ("never sends pricing in the first email," "always offers two times," "no 'just checking in'").

### Their killer deal

Find the deal they named in the CRM, email and calls. Then pick one more recent win yourself, the one that closed fastest or biggest against their usual deal, so you have two to compare. If they said skip, pick both. Read each from first touch to close: the stage changes, every email in both directions, every call, who joined and when, how long each stage took.

Then name the three to five moves that set these deals apart from their usual one: how fast they followed up, what they sent after the demo, how and when they reached more people, how they handled pricing, how they worked with the champion, how they closed. Those moves feed four places:

- **What I do on my best deals** (how-I-work file)
- **What slips:** the same moves, where most of their other deals don't get them
- **Voice examples:** the real emails from these deals
- **Why we win and lose** (sales process file)

If you can't find the deal they named, or it's too new to have a history, say so in Step 3 and study the nearest deal that has one. If they have fewer than two wins, use what there is plus their furthest-along open deal, and say so.

If a rep ran the leader's killer deal, the team's moves go in the sales process file. Only the leader's own part, how they stepped in, goes in their how-I-work file.

### Rep, leader, or both

Work it out while you read. The signals, strongest first:

- **Who owns the deals.** Match their email to a CRM owner. They own most of the open deals: rep. Other people own most and they own few or none: leader. They own a real share and you can see other people's too: both. Being able to see everyone's deals proves nothing by itself, since reps at small companies often have admin access.
- **Team or role data in the CRM.** Teams, a role hierarchy, a manager field.
- **Title.** Their email signature, their CRM user record, a quick web search.
- **Calendar.** Recurring 1:1s, pipeline or forecast reviews, team standups.
- **Email and chat.** Deal reviews, coaching, reps forwarding them threads.

**For a leader, or both:** read the team's deals by owner as well. Look at conversion and time in stage for each rep, the handoffs (SDR to AE, AE to CS), how each rep's pipeline and activity differ, what the top rep does that the others don't, and where the process breaks.

If the signals disagree or there aren't any, don't stop to ask. Save the question for Step 3. If it turns out they lead a team, read the team's deals before you build the files.

### How they work

Work this out from the evidence. Don't ask open questions about strengths or preferences, and leave out anything you can't back up.

- **Best-deal moves.** From the best-deal read, plus whatever their wins and strongest calls share.
- **Where their time goes.** The work they do often and slowly. Timestamps show it: the CRM updated hours or days after a call, recaps that go out late or never, long research before meetings, the same deals checked in on again and again.
- **What slips.** The best-deal moves most of their other deals don't get.
- **Rules.** The always and never patterns in their email and calls.

### Calendar and website

From the calendar, the kinds of meetings they have and how many. From the web, their company site and any resources or case studies page.

The page-building skills need two more things from you, so get both now.

**Customer stories.** Up to five from the site, each with its real URL and headline result. Never write or round a customer's result yourself.

**Their brand: colors, font, logo.** Fetching a page usually gives you the words on it and none of its styling, so one look at the homepage often comes back with nothing. Don't stop there. Work down this list until you have a primary color as a hex code:

1. **The homepage's own tags.** A theme color if it declares one, and the URLs of the logo and the share image.
2. **The site's stylesheet,** if you can open it. Color variables, the color of buttons and links, the font family on headings and body text.
3. **A brand, press or media kit page** on the site, or a search for "[company] brand guidelines."
4. **Their connected docs** (Notion, Google Drive, Confluence). A brand guide, a design system page, or the master deck or proposal template.
5. **The logo or share image itself.** If you can read exact colors out of it, take the main one and mark it "(from the logo, confirm)."

Note where each value came from. If you get to the end with no color, don't guess one, and don't leave a silent blank. Ask for it in Step 3.

## Step 3: Show what you learned, and confirm

Send one message. This is where they should think "it gets me." Make everything in it specific and backed by something you read, and include at least one pattern they probably haven't noticed.

The message always has the same shape: the table of what you read, two sections under headers, then your questions.

- **Section one is about the person.** Who they are, how they sound, how they sell. Words and quotes. Keep the numbers out of it.
- **Section two is about their deals.** This is where the numbers, stages and deal details go, in a table.

For a rep:

```
[the table of what you read]

## You, your voice and how you sell

**Your role.** You carry your own deals, mostly [segment].

**On calls.** You [how they open, or how they handle pricing].
> "[short real quote]"

**In email.** You're [2–3 words]. You open with "[greeting]", close with "[sign-off]", and keep it short.

**A line that's all you.**
> "[real phrase]"

**How you qualify.** You check [methodology, or what they actually check]. [What usually gets missed].

**When a deal goes right.** On your killer deal you [2–3 specific moves].

## A bit about your deals

| | |
|---|---|
| What you sell | [product] to [titles] at [company type, size] |
| Open right now | [N] deals |
| A typical deal | About $[X], about [Y] weeks |
| Your killer deal | [type of deal], and [what made it different, with a number] |
| Your brand | [primary color as hex], [font], from [where you found them] |
| What slips | Most of your other deals don't get [the move that slips most] |
| What's working | [e.g. emails that end on a specific question got a reply 9 of 12 times, against 3 of 14 without one] |

## Two quick questions

1. [Specific question, with the likely answer offered]
2. [Specific question]

A line each is plenty, and fix anything I got wrong. Or just say "looks right."
```

For a leader:

```
[the table of what you read]

## You, your team and how you sell

**Your role.** You lead a team of [N] ([names]) and carry a few deals yourself.

**How you sound.** In email you're [2–3 words]. You open with "[greeting]" and close with "[sign-off]".
> "[real phrase]"

**How the team qualifies.** On [methodology]. [What reps capture, and what usually gets missed].

**When a deal goes right.** On your killer deal, [rep] [2–3 specific moves]. [Top rep] does [habit] and the rest of the team doesn't.

## A bit about your team's deals

| | |
|---|---|
| Open right now | [X] deals across the team |
| A typical deal | About $[X], about [Y] weeks to close |
| How deals really move | [stage → stage → stage] |
| Where they stall | [stage], usually because [reason] |
| Against [competitor] | You win when [reason] and lose when [reason] |
| One thing you may not have seen | [non-obvious team insight, with the number behind it] |
| Your brand | [primary color as hex], [font], from [where you found them] |

## Two quick questions

1. [Specific question]
2. [Specific question]

A line each is plenty, and fix anything I got wrong. Or just say "looks right."
```

For someone who does both, use the rep version. Open **Your role** with both facts ("You lead a team of [N] ([names]) and carry [N] deals yourself"), and add the team's rows (how deals really move, where they stall) to the deals table. Eight rows at most.

Drop any paragraph or row you can't back with something you read during this setup. A short true message beats a long padded one. Give a reply-rate pattern only when each side has at least 8 emails, and give the counts ("9 of 12, against 3 of 14"). Never say "twice as often."

**If you couldn't find their brand.** Make the brand row say "Couldn't find it. See below." Then add this under the deals table. It doesn't count as one of your two questions:

```
**One thing I couldn't find: your brand colors.** Paste your main color as a hex code and your font, or a link to your brand guidelines, and I'll add them. Skip it and your pages will use a plain black-and-white style for now.
```

If they answer, use what they gave you. If they don't, write "Color: not found yet" under `## Brand and proof` and carry on.

**The questions.** Two at most. Each one points at something specific you found, can be answered in a few words, and offers the likely answer when you have one. If the data settled everything, ask one or none. A good question does one of four jobs:

- **Settles a conflict in the data.** "Deals sit in Proposal, but 6 of the 9 there never got a proposal. Does Proposal really mean 'pricing discussed'?"
- **Confirms a rule before you lock it in.** "You never send pricing before a second call. Should I always hold it back?"
- **Picks between real options.** "You and Sam write recaps very differently. Should the team follow yours, his, or neither?"
- **Gets what only they know.** "4 of your 6 losses to [Competitor] came right after a security review. Is security usually what decides it?"

Never ask something generic like "what are you best at?" If you couldn't tell whether they lead a team, spend one question on it ("Do you mostly sell, lead a team, or both?") and leave **Your role** out of the message. If you did state their role, don't ask about it too. They'll correct you if it's wrong.

**Internal chat is background.** What you read in Slack or Teams helps you understand the person and their deals. Use it for that and nothing else. Don't quote their internal messages back to them, and don't name who they were talking to, in the summary or in your questions. Anything you quote in this message comes from their emails to buyers or their calls.

If a source was missing or failed, say so in the paragraph or row it affects and give the fix (see Special cases).

## Step 4: Build the files

Take their corrections and answers, then write the files. Use their real numbers, real stage names and real quotes. Leave live deals out: these files describe how they sell, and they should still be true months from now. Mark anything you inferred without data "(inferred)".

**Scrub every example and quote.** The files stay inside the person's own Claude, but team files get passed around, and all of them need to stay true for months. So buyer details come out. Keep the person's own words exactly and swap the buyer's facts: people become [Buyer], [Champion] or [Rep]; buyer companies become [Company] (competitors keep their names); exact amounts become ranges ("~$40k"); dates become relative ("2 days after the demo"). Cut anything about a deal that's still open. Describe a best deal by its type ("a mid-market win, closed in 5 weeks") and never by name. Start every file with this line: `Sales profile built with Sales Skills by Mutiny (mutinyhq.com) for [Name], [rep / leader / both], on [date].`

Use these `##` headings exactly, in this order. The other Sales Skills find sections by heading. Stay within the word counts. These files are a baseline, so keep them short.

**`mutiny-voice.md`** (theirs, 1,000–1,800 words)
- `## How I sound`: 3–4 specific traits, each with a real example
- `## On calls`: energy, rapport, how I ask questions and handle hard moments
- `## In writing`: greeting, sign-off, length, structure, subject lines, how I ask
- `## By situation`: first follow-up, post-demo recap, check-in, pricing or proposal, scheduling, quick reply. One real example of each, trimmed to about 120 words, taken from best-deal emails first. A second example only for first follow-up and post-demo recap. If a situation has no real example, skip it. Never write one yourself.
- `## Phrases that are mine`: word for word
- `## What gets replies`
- `## Never`: words, phrases and habits that would sound wrong coming from me

**`mutiny-sales-process.md`** (the team's, 400–800 words)
- `## Why we win and lose`: the moves that made the difference on our best deals, and why deals die. Two short paragraphs.
- `## Pipeline stages`: each pipeline and stage in order, with what has to be true to move on, the usual time in stage, and conversion
- `## Discovery and qualification`: the methodology, and what we need to know at each stage
- `## Numbers`: deal size, cycle, win rate, lead sources
- `## Open questions`: anything unresolved, written as a question with the evidence behind it. Leave the section out if there's nothing.

**`mutiny-buyers-and-competitors.md`** (the team's, 350–700 words)
- `## What we sell and who we sell to`: the product in our words, the website and resources page, titles, company type and size, triggers, the buying committee
- `## Pricing and packaging`: real ranges, tiers, how pricing gets presented
- `## Competitors`: a line or two each: when it comes up, and how we usually win or lose
- `## Brand and proof`: primary and accent color (hex), font and logo URL, each with where it came from (the site, a brand guide, or the person). Then customer stories as `[Customer]: [result] ([URL])`. The pricing proposal, business case and deal room skills read this section, so leave out anything you didn't see. If you never found a color, write "Color: not found yet."

**`mutiny-how-i-work.md`** (theirs, 200–500 words)
- `## About me`: name, role, company, and whether I'm a rep, a leader, or both
- `## What I do on my best deals`: protect this and build around it. Say what kind of deal it came from.
- `## Where my time goes`: do this work for me first, without being asked
- `## What slips`: watch for these and tell me
- `## My rules`: always and never
- `## My tools`: what's connected, and what I use that isn't

**`mutiny-how-we-work.md`** (leaders only, the team's, 200–500 words)
- `## Our team`: members, roles, handoffs
- `## Every rep, every deal`: the non-negotiables
- `## What I want to see weekly`
- `## Team rules`

## Step 5: Save

The files live in a Claude project, which is a workspace that keeps its files on hand for every chat inside it. Claude reads project files automatically, so nothing has to go in the project's instructions. Those stay free for the person's own notes and other skills. Every Sales Skill looks these files up by name.

**In Claude:** create the files so they can be downloaded, then walk them through saving. Write it for someone who has never made a project:

```
## Save your profile

One more minute, and every deal chat starts out knowing how you sell.

1. **Download** the files above.
2. **Make a project.** In Claude's left sidebar, click Projects, then New project. Call it "My Deals." A project is a workspace that keeps files for every chat inside it.
3. **Add the files.** On the project page, click + (or Add content) next to Files, choose to upload from your device, and pick the files you just downloaded. They're usually in your Downloads folder.

That's it. Start your deal chats inside My Deals and I'll already sound like you.
```

Adjust it when you need to. If they're already in a project, drop step 2. If this is a refresh, tell them to replace the old files. If the brand is still missing, add one line: "Your pages will use a plain style until I have your brand color. Tell me 'my brand color is #...' any time and I'll update the file."

If you can't make downloadable files here, give each file as its own copyable block with the filename as its title. Have them add each one on the project page: click + next to Files, choose the option to add text content, paste the block, and use the filename (for example `mutiny-voice.md`) as the title.

**Outside Claude** (these skills also run in other AI tools): give each file as a copyable block and tell them to save it wherever their tool keeps standing instructions or attached files. Say nothing about Claude settings or projects.

**For leaders,** add this to the same message:

```
## For your team

Three of these files are your team's: mutiny-sales-process.md, mutiny-buyers-and-competitors.md and mutiny-how-we-work.md. They put every rep on your process while each one keeps their own voice.

To roll them out, send those three files to your reps. Each rep adds them to their own My Deals project and says "Build my sales profile." Setup spots the team files and builds only that rep's voice and how-I-work files.

Want Sales Skills by Mutiny on for every rep without anyone installing it? On a Team or Enterprise plan, your Claude admin can add it for the whole organization from organization settings.

One more thing: you've just written your sales playbook down. If you ever bring your team onto Mutiny, bring these files, and we'll start from how you already sell.
```

**To update later:** they say "Refresh my sales profile." Read the data again, show what changed in a few lines, and replace only the files that changed. If all they give you is a brand color, a font or a link to brand guidelines, update `## Brand and proof` and hand back just that one file.

## Step 6: Run something useful

Close with one offer they can take by saying "yes," run on their real data:

- **Rep:** "Want me to find the 3 deals that need you most this week?" (Mutiny check-in, pipeline scan)
- **Leader or both:** "Want to see which deals across your team have gone quiet, by rep?" (Mutiny check-in, pipeline scan for the team)

After that, and only if you can create scheduled tasks and no daily brief is scheduled yet, add one line: "I can also have your daily brief ready every weekday morning. Want that?" If they say yes, set it for the time they choose.

## Special cases

### Missing, failing or thin sources

**A source fails partway.** Try once more, then move on, and say so in its row of the table: `| CRM | Stopped after 120 deals (connection dropped). Using what I read. |` Build numbers only from what you read, call partial totals partial, and raise it in Step 3 the way you would a missing source. A failed source never holds up setup.

**Thin data.** With fewer than 5 closed deals, skip the won-against-lost comparison and write "Not enough closed deals yet" under `## Why we win and lose`. With no wins, study the two open deals that are furthest along and say that's what you did. With fewer than 10 emails sent to buyers, build the voice from what's there, mark it "(early read, refresh after more emails)", and spend one Step 3 question asking them to paste two or three more.

**No CRM connected.** This is common and it's fine. Calls and email still give you most of the voice, the pitch, the objections, the competitors and the rough path a deal takes. Deal sizes and timelines often turn up in pricing emails and proposals. Rep or leader comes from their title and calendar. In the process file, mark whatever you inferred. Offer to connect the CRM inside the Step 3 message. Don't send a separate one.

**Telling them what's missing (in Step 3).** When a missing connector would have changed something, say so right where it applies and give the fix: "I couldn't see your email, so your voice is a guess. To add it, click your name at the bottom left, then Settings, then Connectors. Not listed? On a work plan, your Claude admin has to add it first." When the CRM isn't connected, put one short block ahead of the questions:

```
I couldn't see your CRM, so your stages and numbers are my best read from calls and email. To sharpen them, connect it (your name at the bottom left, then Settings, then Connectors; on a work plan your admin may need to add it first) or drop a CSV export of your open and closed deals here. Up to you.
```

Read a CSV the way you'd read a CRM: owners, stages, amounts, close dates, won and lost. Run the CRM and best-deal reads again before you build the files.

**Nothing connected at all.** Replace the Step 3 message with one they can skim and answer in short bullets: do you sell, lead a team, or both; what you sell and to whom; your usual deal size and cycle; how leads reach you; your stages; how you qualify (MEDDIC, SPICED, BANT, your own, or nothing formal); your main competitors; what made the deals you named go well; and "paste two or three recent emails you sent to buyers, any will do." Build the voice from those emails.

### The person doesn't seem to sell

Sometimes the person running setup isn't a seller. They might be in marketing or ops, or trying the skills out before rolling them out to a team. The signs: no deals under their name, almost no email to buyers, and a title outside sales.

- **Don't stop, and don't suggest they stop.** They asked for a profile, so build one.
- **Say what you saw, once.** Open the Step 3 message with one line: "I didn't find deals or buyer emails under your name, so this is a thin first pass." Don't guess at why.
- **Build from what there is.** Use whatever they've written to customers, partners or prospects, and the company's deals for the team files, labeled "company-wide." Mark the voice file "(early read, refresh after more emails)."
- **Spend one question on what would help most.** Usually that's asking them to paste two or three emails they've sent to customers.
- **Mention the better test last, as an option.** After the questions, one line: "For a fuller picture, have someone who carries deals run this in their own Claude." Then carry on with their profile.

### Team files already in the project

If `mutiny-sales-process.md`, `mutiny-buyers-and-competitors.md` or `mutiny-how-we-work.md` is already in the project, read its first line.

- **It names someone else as the leader.** The files came from this rep's leader. Read them and don't rebuild them. Tell the rep to delete any earlier copies of their own `mutiny-sales-process.md` and `mutiny-buyers-and-competitors.md`, because the leader's files replace them. Spend the scan on the rep's own email, calls and deals, build `mutiny-voice.md` and `mutiny-how-i-work.md`, and use Step 3 to show what you learned about their voice and deals. Where the rep's habits differ from the team's process, note it in their how-I-work file. Leave the team files alone.
- **It names this person.** This is a refresh. Rebuild them.

## Rules

- **Say only what you verified.** One wrong claim in the first minute ("you use Gong," when they don't) and the "it gets me" moment is gone. If you're not sure, mark it inferred or make it one of your two questions.
- **Two replies, then the save.** People drop off with every extra round. If something is still unclear, mark it inferred or put it under Open questions. Don't ask again.
- **No live deals in the files.** The files have to stay true for months and they get shared with a team. This quarter's deals make them stale and awkward to pass around.
- **Read only.** Never write to the CRM and never send anything. Setup is the first thing people run, and it has to feel completely safe.
- **If they stop partway,** save what you have and tell them they can finish any time with "Refresh my sales profile." Nothing they gave you should be lost.

---

# What every Sales Skill by Mutiny shares (read this before you start)

## Their sales profile

(Running Mutiny setup? Skip this part. Setup is what builds these files.)

The person's sales profile lives in this project as a handful of short files. Find them and use them before you do anything else:

- `mutiny-voice.md`: how they write and talk. Anything you draft as them comes from here.
- `mutiny-sales-process.md`: their stages, what moves a deal forward, how they qualify, why they win and lose.
- `mutiny-buyers-and-competitors.md`: what they sell, who buys it, pricing and competitors, plus `## Brand and proof` (colors, font, logo, customer stories) for anything a buyer will see.
- `mutiny-how-i-work.md`: what they do on their best deals, where their hours go, what slips, and their rules.
- `mutiny-how-we-work.md`, when it's there: what their leader expects on every deal and wants to see each week.

Find a section by its `##` heading. If a team file and a personal file disagree, the team file decides process and rules, and the personal file decides voice and preferences.

No profile at all? Do the job with whatever you can find. Then say once, at the end: "Want me to learn how you sell first? Say 'Build my sales profile'. It takes about 5 minutes, and after that everything I draft sounds like you."

---

## Do the legwork

Before you write anything, see which of the person's tools you can reach, and read what's there. Real data makes the output. A rep shouldn't have to go and fetch something you could have looked up.

**The four that matter most**

- **Their CRM** (HubSpot, Salesforce, Attio and others). Deals, contacts, activity history and notes. When what the rep tells you and what the record says don't match, say so.
- **Their call recorder** (the Mutiny notetaker through the Mutiny connector, Gong, Fireflies, Granola and others). Transcripts and summaries of recent calls with the companies in question.
- **Their email.** The latest threads with the people involved, and the messages the rep sent, which also show how they write.
- **Their calendar.** What's coming up with those same people.

**Worth checking when they're connected**

- **Chat** (Slack, Teams). Two things: what the team is saying internally about the deal, and any direct messages between the rep and the buyer. A buyer message in chat is real contact. Count it when you work out how long a deal has been quiet.
- **Contracts and e-signature** (DocuSign, PandaDoc). What's out for signature and how long it's been sitting there. A contract nobody has signed is a common place for a deal to stall without anyone noticing.
- **Docs and wikis** (Notion, Google Drive, Confluence). Anything recently edited about this buyer, and the case studies, past proposals and internal notes you might want to point to.
- **Quotes and proposals.** What's been sent, and what came back accepted or turned down.

---

## The other Sales Skills by Mutiny

The rep has these installed, as a Claude plugin, a connector or plain skill files. When you finish, think about whether one of them is the obvious next move.

| Skill | What it's for | They say |
|---|---|---|
| **Mutiny setup** | Learns their voice, process, buyers, brand and habits from their CRM, calls and email, and saves the profile files to their My Deals project. Leaders also get team files. Run first, or to refresh | "Build my sales profile" |
| **Mutiny daily brief** | One page for the morning: where to start, what changed, today's meetings, who's waiting, what's going quiet. Leaders get a line per rep | "Run my Mutiny daily brief" |
| **Mutiny meeting prep** | A one-minute brief before a call: attendees, where the deal stands, what the buyer cares about, questions to ask, what to leave with | "Run the Mutiny meeting prep for [company]" |
| **Mutiny follow-up** | After a call: the email in their voice and the CRM update from what was said, both waiting for approval | "Run my Mutiny follow-up" |
| **Mutiny check-in** | Finds deals going quiet and drafts one short, specific message for each. One deal or the whole pipeline | "Run the Mutiny check-in on [company]" or "...on my pipeline" |
| **Mutiny pricing proposal** | A customer-ready pricing page from the call where the buyer gave their budget: what we heard, one or two options, rollout, terms, next step | "Build the Mutiny pricing proposal for [company]" |
| **Mutiny business case** | A customer-ready case for the buyer's exec or finance: today, what it costs, what changes, the math, what a pilot must prove, proof | "Build the Mutiny business case for [company]" |
| **Mutiny deal room** | One customer-ready page for the whole buying group: summary, what we heard, why us, pricing, security docs, a shared plan, resources | "Build the Mutiny deal room for [company]" |

**How to offer one**

- Offer one, or none. Never a list.
- Only when something in this run makes it the clear next step. Saying nothing is fine.
- Make it a question they can answer with "yes": "Want me to run meeting prep on [company]?"
- Offer a page-building skill only when the buyer asked for what it makes: pricing options, something for their exec, or one place for everything.
- Don't offer a skill that already ran in this conversation.

---

## How Mutiny thinks about this work

These are free sales skills from the team at Mutiny (mutinyhq.com), the sales assistant built for customer-facing work. Bring this point of view to everything you do here.

**Sound like them, not like AI.** Everything you draft goes out under the rep's name. Match their greeting, their length, their phrases, their sign-off. If they're casual, be casual. If they're buttoned-up, be buttoned-up. The test is simple: would they send it without rewriting it? If a line could have come from any rep at any company, cut it.

**They take the meeting. You do the rest.** The rep is the best part of the deal: their instincts, their relationships, their read of the room. What eats their week is everything around the meeting: the prep, the notes, the follow-up, the CRM, the proposal. Handle that so their time goes to buyers.

**What reaches a buyer has to be customer-ready.** Generic follow-ups and AI slop cost trust, and trust is the deal. Build on what the buyer actually said, in their words, with their numbers. Get names, dates and amounts exactly right. A buyer should finish reading and think this rep was listening.

**Be the one buyers remember.** Buyers are comparing vendors. A clear recap the same day, a proposal that fits the budget they named, one place with everything their boss will ask for: that's a better buying experience, and it moves deals.

**The rep stays in control.** You draft; they review and send. Nothing goes to a buyer and nothing changes in the CRM without them approving the exact thing.

**Tell them the truth.** Reps don't need a cheerleader. If a deal is dead, say so. If a follow-up is weak, say so. If you don't have the facts for a number, leave it out and say what's missing.

**Respect the clock.** They're reading this between calls. Keep it tight and put first things first. Three things that matter beat ten that might.

<!-- Sales Skills by Mutiny (mutinyhq.com), Apache-2.0. Adapted in part from Sales Skills by Arrows (github.com/ArrowsHQ/arrows-sales-skills, Apache-2.0); modified by Mutiny. See NOTICE. -->
