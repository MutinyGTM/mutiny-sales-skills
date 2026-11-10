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
