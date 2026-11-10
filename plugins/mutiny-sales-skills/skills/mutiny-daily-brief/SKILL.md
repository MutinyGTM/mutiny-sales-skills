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
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mutiny</title>
<style>
:root{color-scheme:light;--purple:#A73BF5;--lilac:#F2D1FC;--lime:#B2FF14;--lime-soft:#D2FD78;--coral:#FB5A3D;--coral-ink:#B92C12;--coral-soft:#FFE1DA;--purple-ink:#6A1BA6;--ink:#000;--ink-2:rgba(0,0,0,.72);--ink-3:rgba(0,0,0,.54);--rule:rgba(0,0,0,.14);--page:#FFFFFF;--soft:#F4F4F2;--serif:'Reckless Condensed S',Georgia,'Times New Roman',serif;--sans:'KMR Waldenburg',Arial,Helvetica,sans-serif}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--page);color:var(--ink);font:15px/1.5 var(--sans);-webkit-font-smoothing:antialiased}
.sheet{max-width:780px;margin:0 auto;padding:0 0 48px}
.top{background:var(--lilac);padding:26px 24px 22px;border-radius:0 0 22px 22px}
.kind{font-size:12px;font-weight:700;letter-spacing:1.4px;text-transform:uppercase}
.top h1{font:400 44px/1.02 var(--serif);letter-spacing:-.3px;margin:10px 0 6px;text-wrap:balance}
.top .sub{font-size:16px;margin:0;color:var(--ink-2)}
.top .note{font-size:14px;margin:6px 0 0;color:var(--ink-2)}
.alert{margin:14px 0 0;background:var(--coral);border-radius:10px;padding:8px 12px;font-size:14px;font-weight:700}
.tiles{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;margin-top:18px}
.tile{display:block;background:var(--page);border-radius:14px;padding:12px 14px;color:inherit;text-decoration:none;min-width:0}
a.tile:hover{outline:2px solid var(--ink)}
.tile .n{font:400 30px/1.05 var(--serif);font-variant-numeric:tabular-nums;overflow-wrap:anywhere}
.tile .l{font-size:12px;color:var(--ink-2);margin-top:2px}
.body{padding:0 24px}
section{margin-top:34px;scroll-margin-top:12px}
.sh{display:flex;justify-content:space-between;align-items:baseline;gap:12px;border-top:3px solid var(--ink);padding-top:10px}
.sh h2{font:400 26px/1.1 var(--serif);margin:0}
.sh span{font-size:12px;color:var(--ink-3);text-align:right}
.row{display:grid;grid-template-columns:44px minmax(0,1fr);gap:0 10px;padding:13px 0;border-bottom:1px solid var(--rule)}
.lead{font:400 20px/1.2 var(--serif);font-variant-numeric:tabular-nums;padding-top:1px}
.lead.t{font:700 13px/1.6 var(--sans)}
.dot{width:12px;height:12px;border-radius:3px;background:var(--rule);margin-top:5px}
.dot.good{background:var(--lime);box-shadow:inset 0 0 0 1px rgba(0,0,0,.4)}
.dot.bad{background:var(--coral)}
.dot.open{background:var(--purple)}
.ti{font-weight:700}
.me{font-size:13px;color:var(--ink-3);margin-left:6px;font-variant-numeric:tabular-nums}
.pill{display:inline-block;font-size:12px;font-weight:700;border-radius:999px;padding:1px 9px;margin-left:6px;background:var(--soft);color:var(--ink-2);white-space:nowrap;vertical-align:1px}
.pill.bad{background:var(--coral-soft);color:var(--coral-ink)}
.pill.good{background:var(--lime-soft);color:var(--ink)}
.pill.open{background:var(--lilac);color:var(--purple-ink)}
.ln{font-size:13px;color:var(--ink-3);font-variant-numeric:tabular-nums}
.tx{color:var(--ink-2)}
.qt{font:400 16px/1.4 Georgia,'Times New Roman',serif;font-style:italic;margin-top:2px}
.nx{margin-top:4px;font-weight:700}
.nx::before{content:"Next: ";font-weight:400;color:var(--ink-3)}
.src{font-size:12px;color:var(--ink-3);margin-top:2px}
details.more{margin-top:6px}
details.more summary{cursor:pointer;font-size:13px;color:var(--purple-ink);font-weight:700;width:fit-content}
details.more .in{margin-top:6px;background:var(--soft);border-radius:10px;padding:10px 12px;font-size:13px;color:var(--ink-2)}
details.more ol,details.more ul{margin:0;padding-left:18px}
details.more ol{color:var(--ink)}
details.more ol+ul{margin-top:8px}
details.more li+li{margin-top:3px}
.none{padding:12px 0;color:var(--ink-3);border-bottom:1px solid var(--rule)}
.foot{font-size:13px;color:var(--ink-3);padding-top:10px}
footer{margin:38px 24px 0;font-size:12px;color:var(--ink-3)}
footer summary{cursor:pointer}
footer p{max-width:640px;margin:8px 0 0}
footer a{color:var(--ink-2)}
footer .by{margin-top:14px}
@media (max-width:560px){.tiles{grid-template-columns:repeat(2,minmax(0,1fr))}.top{padding:22px 16px 18px}.top h1{font-size:34px}.body{padding:0 16px}footer{margin:34px 16px 0}.row{grid-template-columns:36px minmax(0,1fr)}}
</style>
</head>
<body>
<div class="sheet" id="page"></div>
<script>
/* Fill in DATA only. Leave everything else as is. */
const DATA = {
  kind: "[Daily brief | Meeting prep]",
  title: "[The page's headline]",
  sub: "[One line under it]",
  notes: [],
  alert: "",
  tiles: [],
  sections: [],
  updated: "[date, time]",
  built: "[What was read, and anything missing]"
};

const ABOUT = {
  "Daily brief": [
    "This page is put together fresh each time from the calendar, CRM, email and calls. The sections always come in the same order. It only reads those tools. Nothing in the CRM, an inbox or a calendar was changed.",
    "While you were out covers buyer replies, stage changes, wins, losses and signed contracts since the start of the last working day. A deal lands in Going quiet for one of three reasons: no reply, call or meeting with the buyer in 14 or more days, no dated next step, or a promised next step that didn't happen. Waiting on you lists buyers who wrote last and haven't heard back. Today's meetings shows sales calls only."
  ],
  "Meeting prep": [
    "This page is put together fresh before each call from the calendar, CRM, email and calls. The sections always come in the same order. It only reads those tools. Nothing in the CRM, an inbox or a calendar was changed. It's for the seller. The buyer never sees it.",
    "Questions to ask come from what the team needs to know at this stage and doesn't know yet. Labels on attendees, such as champion or skeptic, appear only when a call or an email backs them up. Every line says where it came from."
  ]
};
const safe = v => String(v ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const arr = v => (Array.isArray(v) ? v : v ? [v] : []).filter(Boolean);
const tone = t => ["good", "bad", "open"].includes(t) ? " " + t : "";
const slug = s => String(s || "").toLowerCase().replace(/[^a-z0-9]+/g, "-");
function row(r) {
  const lead = r.lead ? `<div class="lead${/[:apm]/i.test(r.lead) ? " t" : ""}">${safe(r.lead)}</div>` : `<div><div class="dot${tone(r.mark)}"></div></div>`;
  const head = (r.title || r.meta || r.tag) ? `<div>${r.title ? `<span class="ti">${safe(r.title)}</span>` : ""}${r.meta ? `<span class="me">${safe(r.meta)}</span>` : ""}${r.tag ? `<span class="pill${tone(r.tone)}">${safe(r.tag)}</span>` : ""}</div>` : "";
  const steps = arr(r.steps), more = arr(r.more);
  const extra = steps.length || more.length ? `<details class="more"><summary>${steps.length ? "How" : "Details"}</summary><div class="in">${steps.length ? `<ol>${steps.map(s => `<li>${safe(s)}</li>`).join("")}</ol>` : ""}${more.length ? `<ul>${more.map(s => `<li>${safe(s)}</li>`).join("")}</ul>` : ""}</div></details>` : "";
  return `<div class="row">${lead}<div>${head}${arr(r.lines).map(l => `<div class="ln">${safe(l)}</div>`).join("")}${r.text ? `<div class="tx">${safe(r.text)}</div>` : ""}${r.quote ? `<div class="qt">“${safe(r.quote)}”</div>` : ""}${r.next ? `<div class="nx">${safe(r.next)}</div>` : ""}${r.source ? `<div class="src">${safe(r.source)}</div>` : ""}${extra}</div></div>`;
}
const P = DATA, secs = arr(P.sections);
let out = `<header class="top"><div class="kind">${safe(P.kind)}</div><h1>${safe(P.title)}</h1>${P.sub ? `<p class="sub">${safe(P.sub)}</p>` : ""}${arr(P.notes).map(n => `<p class="note">${safe(n)}</p>`).join("")}${P.alert ? `<div class="alert">${safe(P.alert)}</div>` : ""}`;
if (arr(P.tiles).length) out += `<div class="tiles">${arr(P.tiles).map(t => t.to ? `<a class="tile" href="#${slug(t.to)}"><div class="n">${safe(t.n)}</div><div class="l">${safe(t.label)}</div></a>` : `<div class="tile"><div class="n">${safe(t.n)}</div><div class="l">${safe(t.label)}</div></div>`).join("")}</div>`;
out += `</header><div class="body">`;
out += secs.map(s => `<section id="${slug(s.id || s.title)}"><div class="sh"><h2>${safe(s.title)}</h2><span>${safe(s.hint)}</span></div>${arr(s.rows).length ? arr(s.rows).map(row).join("") : `<div class="none">${safe(s.empty || "Nothing here today.")}</div>`}${s.foot ? `<div class="foot">${safe(s.foot)}</div>` : ""}</section>`).join("");
out += `</div><footer><details><summary>How this page works</summary>${(ABOUT[P.kind] || []).map(p => `<p>${safe(p)}</p>`).join("")}<p>This run: ${safe(P.built)}</p></details><div class="by">Updated ${safe(P.updated)} · Built with Sales Skills by <a href="https://www.mutinyhq.com/?utm_source=sales-skills&utm_medium=report&utm_campaign=${slug(P.kind)}" target="_blank" rel="noopener">Mutiny</a></div></footer>`;
document.getElementById("page").innerHTML = out;
document.title = [P.kind, P.title].filter(Boolean).join(" · ");
</script>
</body>
</html>
```

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
