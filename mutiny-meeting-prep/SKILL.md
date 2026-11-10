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
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Meeting prep</title>
<style>
:root{
  color-scheme:light;
  --paper:#EFEFEF; --card:#FFFFFF; --ink:#000000; --ink-70:rgba(0,0,0,.7); --ink-50:rgba(0,0,0,.58); --ink-30:rgba(0,0,0,.3);
  --line:#E0E0E0; --chip:#EFEFEF; --track:#E0E0E0;
  --green:#B2FF14; --green-soft:#D2FD78;
  --red:#D93A1B; --red-soft:#FFE1DA;
  --gold:#A73BF5; --gold-soft:#F2D1FC; --gold-text:#6A1BA6;
  --display:'KMR Waldenburg',Arial,Helvetica,sans-serif; --serif:'Reckless Condensed S',Georgia,'Times New Roman',serif;
}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font:14px/1.5 'KMR Waldenburg',Arial,Helvetica,sans-serif;-webkit-font-smoothing:antialiased}
.wrap{max-width:960px;margin:0 auto;padding:16px 16px 40px}
.num{font-variant-numeric:tabular-nums}
.chip{display:block;font-family:var(--display);font-size:18px;font-weight:700;letter-spacing:-.2px;color:var(--ink)}
.hero{background:#000000;color:#FFFFFF;position:relative;border-radius:4px;padding:20px 24px 18px}
.hero h1{font-family:var(--serif);font-feature-settings:"lnum","tnum";color:#FFFFFF;font-size:40px;line-height:1.05;letter-spacing:-.3px;font-weight:400;margin:0 0 4px;max-width:760px}
.hero .sub{color:rgba(255,255,255,.75);font-size:15px;margin:0 0 16px}
.health{display:flex;height:10px;border-radius:2px;overflow:hidden;background:rgba(250,248,245,.15)}
.g-fill{background:var(--green)}
.r-fill{background:var(--red)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);margin-top:14px;border-top:1px solid rgba(250,248,245,.16)}
.stat{padding:14px 12px 0 0}
.stat+.stat{padding-left:16px;border-left:1px solid rgba(250,248,245,.16)}
.stat .n{font-family:var(--serif);font-feature-settings:"lnum","tnum";font-size:32px;font-weight:400;letter-spacing:-.3px;line-height:1.15}
.stat .l{font-size:12px;color:rgba(255,255,255,.75)}
.stat .key{display:inline-block;width:8px;height:8px;border-radius:2px;margin-right:6px;vertical-align:1px}
.card{background:var(--card);border:1px solid var(--line);border-radius:4px;padding:20px 22px;margin-top:16px}
.head{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px;padding-bottom:10px;border-bottom:1px solid var(--line)}
.hint{font-size:12px;color:var(--ink-50)}
.item{border-top:1px solid var(--line)}
.head + .item{border-top:0}
.row{display:grid;grid-template-columns:26px 1fr 14px;gap:6px;padding:10px 0;align-items:start}
details.item summary{list-style:none;cursor:pointer}
details.item summary::-webkit-details-marker{display:none}
details.item summary .row::after{content:"";width:7px;height:7px;border-right:1.5px solid var(--ink-30);border-bottom:1.5px solid var(--ink-30);transform:rotate(-45deg);margin-top:7px;transition:transform .15s}
details.item[open] summary .row::after{transform:rotate(45deg)}
details.item summary:hover .row::after{border-color:var(--ink-70)}
.mark.dot::before{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--ink-30);margin-top:6px}
.mark.dot.r::before{background:var(--red)}
.mark.dot.g::before{background:var(--green);box-shadow:0 0 0 1px rgba(0,0,0,.35)}
.tick{width:16px;height:16px;border-radius:50%;background:var(--green);color:#000;font-size:10px;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:2px}
.title{font-weight:600}
.who{font-size:12px;color:var(--ink-50);font-weight:400;margin-left:6px}
.sub2{font-size:13px;color:var(--ink-70)}
.detail{margin:0 20px 12px 28px;padding:10px 12px;background:#F5F5F5;border-radius:6px;font-size:13px;color:var(--ink-70)}
.detail ul,.detail ol{margin:0;padding-left:18px}
.detail ol li{color:var(--ink)}
.detail .ctx{margin-top:8px;font-size:12px;color:var(--ink-50)}
a.stat{display:block;color:inherit;text-decoration:none;cursor:pointer}
a.stat:hover .l{text-decoration:underline;text-underline-offset:2px}
section[id]{scroll-margin-top:12px}
.cols{display:grid;grid-template-columns:1fr 1fr}
.cols > .item:nth-child(odd){padding-right:22px;border-right:1px solid var(--line)}
.cols > .item:nth-child(even){padding-left:22px}
.num-badge{width:22px;height:22px;border-radius:50%;background:var(--ink);color:#fff;font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:-1px}
.cols > .item:nth-child(-n+2){border-top:0}
.detail li+li{margin-top:3px}
.next{color:var(--ink);font-size:13px}
.next::before{content:"→ ";color:var(--ink-30)}
.qline{margin:3px 0 2px}
.tag.r{background:var(--red-soft);color:var(--red)}
.tag.g{background:var(--green-soft);color:var(--green)}
.tag.n{background:var(--chip);color:var(--ink-70)}
.empty{font-size:13px;color:var(--ink-50);padding:6px 0}
.rep-row{display:grid;grid-template-columns:190px 1fr;gap:12px}
.minibar{display:flex;height:8px;border-radius:2px;overflow:hidden;background:var(--track);margin-top:6px;max-width:220px}
.more{font-size:12px;color:var(--ink-50);padding-top:10px;border-top:1px solid var(--line)}
.r-al{text-align:right}
.meta{font-size:12px;color:var(--ink-50)}
footer{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-top:20px;font-size:12px;color:var(--ink-50)}
footer details summary{cursor:pointer}
footer a{color:var(--ink-70);text-decoration:underline;text-underline-offset:2px}
footer a:hover{color:var(--ink)}
.about{max-width:680px;margin-top:6px;padding:12px 14px;background:var(--card);border:1px solid var(--line);border-radius:4px;color:var(--ink-70);font-size:13px}
.about p{margin:0 0 8px}
.about p:last-child{margin:0}
.about b{color:var(--ink);font-weight:600}
.tag.g{color:#000!important}
.y-fill{background:var(--gold)}
.mark.dot.y::before{background:var(--gold)}
.tag.y{background:var(--gold-soft);color:var(--gold-text)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px;align-items:start}
.grid2 .card,.grid3 .card{margin-top:0}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:16px;align-items:start}
.card.won{border-top:3px solid var(--green)}
.card.lost{border-top:3px solid var(--red)}
.card.won .head,.card.lost .head{border-bottom:0}
.mark{font-weight:700;color:var(--ink-30);font-size:14px}
.tag{display:inline-block;font-size:12px;font-weight:600;border-radius:2px;padding:1px 6px;white-space:nowrap;margin-left:6px}
.qline .tag{margin-left:0}
.stage{display:grid;grid-template-columns:170px 1fr 100px;gap:14px;align-items:center;padding:9px 0;border-top:1px solid var(--line)}
.head + .stage{border-top:0}
.stage .bar{display:flex;height:12px;border-radius:2px;overflow:hidden}
.stage .gap{grid-column:2/4;font-size:12px;color:var(--ink-50);margin-top:-6px}
.legend{display:flex;gap:16px;font-size:12px;color:var(--ink-50);margin-top:10px}
.legend i{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:5px;vertical-align:-1px}
footer details p{max-width:640px;margin:6px 0 0}
@media (max-width:720px){
  .hero{padding:22px 18px 18px}
  .hero h1{font-size:30px}
  .stats{grid-template-columns:repeat(2,1fr)}
  .stat:nth-child(3){padding-left:0;border-left:0}
  .stat:nth-child(n+3){margin-top:10px}
  .grid2,.grid3,.cols{grid-template-columns:1fr}
  .cols > .item:nth-child(2){border-top:1px solid var(--line)}
  .cols > .item:nth-child(odd){padding-right:0;border-right:0}
  .cols > .item:nth-child(even){padding-left:0}
  .card{padding:16px}
  .detail{margin:0 0 12px 28px}
  .rep-row{grid-template-columns:1fr;gap:4px}
  .stage{grid-template-columns:1fr 90px}
  .stage .bar{grid-column:1/3}
  .stage .gap{grid-column:1/3;margin-top:0}
}
.hero .stat .n{font-size:22px}
@media (max-width:720px){.hero .stat .n{font-size:18px}}
</style>
</head>
<body>
<div class="wrap" id="app"></div>
<script>
/* Fill in DATA only. Leave everything else as is. */
const DATA = {
  name: "[First name]",
  company: "[Buyer company]",
  when: "[Weekday Month Day · time · length]",
  callNumber: "[Call N | First call]",
  agenda: "",
  theyWant: "",
  deal: { stage: "", amount: null, close: "", owner: "" },
  atRisk: "",
  note: "",
  updated: "[date, time]",
  numbers: { gaps: 0, owed: 0 },
  want: [],
  watch: [],
  push: [],
  people: [],
  lastTime: [],
  unknown: [],
  words: [],
  howBuilt: "[What was read, anything missing]"
};

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const money = n => n == null || n === "" ? "" : n >= 1e6 ? "$" + (n / 1e6).toFixed(1).replace(/\.0$/, "") + "M" : n >= 1e3 ? "$" + Math.round(n / 1e3) + "k" : "$" + n;
const list = a => (a || []).filter(Boolean);
const detailBox = d => {
  const lines = Array.isArray(d) ? list(d) : d ? [d] : [];
  return lines.length ? `<div class="detail"><ul>${lines.map(l => `<li>${esc(l)}</li>`).join("")}</ul></div>` : "";
};
const stepsBox = (steps, context) => {
  const st = list(steps);
  if (!st.length && !context) return "";
  return `<div class="detail">${st.length ? `<ol>${st.map(x => `<li>${esc(x)}</li>`).join("")}</ol>` : ""}${context ? `<div class="ctx">${esc(context)}</div>` : ""}</div>`;
};
const item = (mark, title, sub, detail, box0) => {
  const body = `<div class="row">${mark}<div>${title}${sub ? `<div class="sub2">${sub}</div>` : ""}</div></div>`;
  const box = box0 || detailBox(detail);
  return box ? `<details class="item"><summary>${body}</summary>${box}</details>` : `<div class="item">${body}</div>`;
};
const src = s => s ? `<span class="who">${esc(s)}</span>` : "";
const flagTag = f => !f ? "" : `<span class="tag ${f === "skeptic" ? "r" : f === "champion" ? "g" : "n"}">${esc(f)}</span>`;
const D = DATA, N = D.numbers, dl = D.deal || {};
const go = id => `href="#${id}" onclick="const t=document.getElementById('${id}');if(t){t.scrollIntoView({behavior:'smooth'});}return false;"`;
const cols = items => items.length ? `<div class="cols">${items.join("")}</div>` : "";
const card = (title, hint, body, empty, id) => `<section class="card"${id ? ` id="${id}"` : ""}><div class="head"><span class="chip">${title}</span><span class="hint">${hint || ""}</span></div>${body || `<div class="empty">${empty}</div>`}</section>`;

let h = "";
h += `<section class="hero"><h1>${esc(D.name)}'s meeting prep: ${esc(D.company)}</h1><p class="sub">${esc([D.when, D.callNumber].filter(Boolean).join(" · "))}</p>`;
if (D.agenda || D.theyWant) h += `<p class="sub">${D.agenda ? "Agenda: " + esc(D.agenda) : ""}${D.agenda && D.theyWant ? "<br>" : ""}${D.theyWant ? "They want: " + esc(D.theyWant) : ""}</p>`;
if (D.note) h += `<p class="sub">${esc(D.note)}</p>`;
h += `<div class="stats num">
  <div class="stat"><div class="n">${esc(dl.stage || "No deal")}</div><div class="l">${esc(dl.owner ? "Owner: " + dl.owner : "Stage")}</div></div>
  <div class="stat"><div class="n">${money(dl.amount) || "–"}</div><div class="l">${esc(dl.close ? "Close " + dl.close : "Amount")}</div></div>
  <a class="stat" ${go("unknown")}><div class="n">${N.gaps}</div><div class="l"><span class="key y-fill"></span>Still unknown</div></a>
  <a class="stat" ${go("owed")}><div class="n">${N.owed}</div><div class="l">Open commitments</div></a>
</div>${D.atRisk ? `<p class="sub" style="margin:14px 0 0"><span class="tag r" style="margin-left:0">At risk</span> ${esc(D.atRisk)}</p>` : ""}</section>`;

h += card("What they want to solve", "", cols(list(D.want).map(w => item(`<span class="tick">✓</span>`, `<span class="title">${esc(w.point)}</span>${src(w.source)}`, w.quote ? "“" + esc(w.quote) + "”" : "", w.detail))), "Nothing stated by the buyer yet.");
h += card("Watch out for", "", cols(list(D.watch).map(w => item(`<span class="mark dot r"></span>`, `<span class="title">${esc(w.risk)}</span>${src(w.source)}`, `<div class="next">${esc(w.handle)}</div>`, w.detail))), "No risks found for this call.");

h += `<section class="card"><div class="head"><span class="chip">What to push for</span><span class="hint">Open any item for how</span></div><div class="cols">`;
h += list(D.push).length ? list(D.push).map((p, i) => item(`<span class="num-badge">${i + 1}</span>`, `<span class="title">${esc(p.outcome)}</span>`, esc(p.why), null, stepsBox(p.steps, p.context) || detailBox(p.why ? [p.why] : []))).join("") : `<div class="empty">Not enough deal context for specific pushes.</div>`;
h += `</div></section>`;

h += card("Who's on the call", list(D.people).length || "", cols(list(D.people).map(p => item(`<span class="mark dot ${p.flag === "skeptic" ? "r" : p.flag === "champion" ? "g" : ""}"></span>`, `<span class="title">${esc(p.name)}</span><span class="who">${esc(p.title)}</span>${flagTag(p.flag)}`, `${esc(p.role)}${src(p.source)}`, p.detail))), "No attendee list found.", "people");
h += card("Last time and what's owed", "", cols(list(D.lastTime).map(l => item(l.status === "done" ? `<span class="tick">✓</span>` : `<span class="mark dot ${l.status === "open" ? "y" : ""}"></span>`, `${esc(l.text)}${l.status === "open" ? `<span class="tag y">open</span>` : ""}${src(l.source)}`, "", l.detail))), "First call. No prior touchpoints.", "owed");

h += card("Still unknown", "", cols(list(D.unknown).map(u => item(`<span class="mark dot y"></span>`, `<span class="title">${esc(u.item)}</span>`, esc(u.why), u.detail))), "No open gaps for this stage.", "unknown");
h += card("Their words", "", cols(list(D.words).map(w => item(`<span class="mark">“</span>`, `${esc(w.phrase)}${src(w.source)}`, "", ""))), "No direct quotes yet.");

h += `<footer><details><summary>How this report works</summary><div class="about">
<p>This page is rebuilt from the calendar, CRM, email and calls before each call. The layout and order never change, so each section is always in the same place. It reads those tools and nothing more: nothing in the CRM, an inbox or a calendar was changed. It's written for the seller. The buyer never sees it.</p>
<p><b>Still unknown</b> checks the deal against the team's own way of qualifying, taken from the sales profile. A deal is <b>at risk</b> when there's been no two-way contact in 14 or more days, there's no dated next step, or a promised next step didn't happen. <b>Champion</b>, <b>skeptic</b> and <b>decision maker</b> appear only when a call or an email backs them up.</p>
<p>Every line says where it came from. Open the arrow on any row for more.</p>
<p><b>This time:</b> ${esc(D.howBuilt)}</p></div></details><span>Updated ${esc(D.updated)} · Built with Sales Skills by <a href="https://www.mutinyhq.com/?utm_source=sales-skills&utm_medium=report&utm_campaign=meeting-prep" target="_blank" rel="noopener">Mutiny</a></span></footer>`;
document.getElementById("app").innerHTML = h;
</script>
</body>
</html>
```

---

# Shared context for every Sales Skill (read before starting)

## The person's sales profile

(If the skill you're running is Mutiny setup, skip this section: setup builds these files.)

Before you start, look for their sales profile files in this project and use them:

- `mutiny-voice.md`: how they write and talk. Use it for anything you draft as them.
- `mutiny-sales-process.md`: stages, what moves a deal, methodology, why they win and lose.
- `mutiny-buyers-and-competitors.md`: what they sell, who buys, pricing, competitors, and `## Brand and proof` (their colors, font, logo and customer stories) for anything a buyer will see.
- `mutiny-how-i-work.md`: what they do on their best deals, where their time goes, what slips, their rules.
- `mutiny-how-we-work.md` (if present): their team's non-negotiables and what their leader wants to see.

Look sections up by their `##` heading. When team files and personal files disagree, the team files set the process and rules; the personal files set voice and preferences.

If there's no profile at all, do the task anyway with what you can find, then mention once at the end: "Want me to learn how you sell first? Say 'Build my sales profile'. It takes about 5 minutes and makes everything I draft sound like you."

---

## Before you start

Check what other tools and data sources you have access to. Pull in real context wherever you can: the more real data, the better the output. Don't ask the rep to go find information you can look up yourself.

**Core sources:**
- **CRM (HubSpot, Salesforce, Attio, etc.):** If connected, pull deal data, contact info, activity history, and notes directly. Cross-reference what the rep says with what's actually in the CRM.
- **Call recordings (the Mutiny notetaker through the Mutiny connector, Gong, Fireflies, Granola, etc.):** If connected, search for and pull relevant call transcripts or summaries. Look for recent calls with the companies mentioned.
- **Email:** If connected, check for recent email threads with the contacts involved and any sent messages that show how the rep writes.
- **Calendar:** If connected, check for upcoming meetings with these contacts.

**Extra sources (often overlooked but high value):**
- **Chat (Slack, Teams, etc.):** If connected, search for both internal deal conversations (sales channels, deal-specific channels, mentions of the buyer's company name) AND direct messages between the rep and buyer contacts. Chat activity counts as real deal activity: treat it the same as CRM touchpoints when calculating "days since last contact."
- **Contracts and signing (DocuSign, PandaDoc, etc.):** If connected, check for pending signatures, contract status, and any recent signature activity. Contracts sitting unsigned are often where deals quietly die.
- **Documents and knowledge (Notion, Google Drive, Confluence, etc.):** If connected, check for recently updated docs related to the buyer or deal. Also useful for finding case studies, collateral, past proposals or internal notes to reference.
- **Quoting and proposals (CPQ tools, etc.):** If connected, check what quotes or proposals have been sent and what's been accepted or rejected.

Use everything you find. The rep's time is valuable, so do the legwork for them.

---

## The Mutiny skills available to suggest

Below are the Sales Skills by Mutiny the rep has installed (as a Claude plugin, a connector, or standalone skill files). When you finish the skill you're running, look at what came up and offer ONE relevant next Mutiny skill if it would really help. A concrete suggestion, not a pile. Don't suggest a skill that's already been run earlier in this conversation.

**Mutiny setup**: builds the person's sales profile (voice, sales process, buyers, competitors, brand and proof, how they work) from their CRM, calls and email, with two quick replies. Saves it as mutiny-*.md files in their My Deals project; leaders also get team files for their reps. Run first, or to refresh. Trigger: "Build my sales profile."

**Mutiny daily brief**: a short read for the start of the day, built for a phone: what to do first, what changed since yesterday, today's calls with deal context, replies waiting, deals at risk and open time. Leaders also get a line per rep. Trigger: "Run my Mutiny daily brief."

**Mutiny meeting prep**: a 60-second brief for one upcoming call: who you're meeting, what they want to solve, what's owed on both sides, what you still don't know for your qualification method, what to push for and what could go sideways. Finds the call by itself. Trigger: "Run the Mutiny meeting prep for [company]."

**Mutiny follow-up**: right after a call: finds the most recent call, drafts the follow-up in the person's voice, and prepares the CRM update from what was said (next step, stage, competitors, follow-up tasks with dates), applied only after they approve the exact changes. Trigger: "Run my Mutiny follow-up."

**Mutiny check-in**: gets quiet deals moving: check in on one deal, or scan the pipeline for deals at risk and draft check-ins for the top ones, with one play per deal in the person's voice. Leaders get it by rep. Trigger: "Run the Mutiny check-in on [company]" or "Run the Mutiny check-in on my pipeline."

**Mutiny pricing proposal**: a customer-ready pricing page built from the call where the buyer shared budget and requirements: what we heard, one or two options inside their range, what's included, rollout, terms and the next step. In the seller's brand, for the buyer to forward. Trigger: "Build the Mutiny pricing proposal for [company]."

**Mutiny business case**: a customer-ready executive business case the champion can take to their exec or finance: current state, what it costs, the future state, benefits with the math shown, what a pilot must prove, and customer proof. Numbers only from the buyer or the seller's own material. Trigger: "Build the Mutiny business case for [company]."

**Mutiny deal room**: one customer-ready page for the whole buying group: executive summary, what we heard, why us, pricing, security and legal, a shared plan with owners and dates on both sides, and resources. Rebuilt after each call. Trigger: "Build the Mutiny deal room for [company]."

**Rules for suggesting:**
- Only suggest when there's a real, specific reason to. Silence is fine.
- One suggestion per skill run. Not a menu.
- Frame it as a concrete offer the rep can accept in one word: "Want me to run meeting prep on [company]?" Not "You could also consider meeting prep."
- Suggest an asset skill only when the buyer asked for what it makes: pricing options, something for their exec, or one place for everything.
- Don't re-suggest a skill that was already run in this conversation.

---

## The Mutiny perspective

You're running a skill from Sales Skills by Mutiny. These are free sales skills built by the team at Mutiny (mutinyhq.com), the sales assistant built for customer-facing work. Here's the perspective to bring to this work:

**Sound like them, not like AI.** Everything you draft goes out under the rep's name. Match their greeting, their length, their phrases, their sign-off. If they're casual, be casual. If they're buttoned-up, be buttoned-up. The test is simple: would they send it without rewriting it? If a line could have come from any rep at any company, cut it.

**They take the meeting. You do the rest.** The rep is the best part of the deal: their instincts, their relationships, their read of the room. What eats their week is everything around the meeting: the prep, the notes, the follow-up, the CRM, the proposal. Handle that so their time goes to buyers.

**What reaches a buyer has to be customer-ready.** Generic follow-ups and AI slop cost trust, and trust is the deal. Build on what the buyer actually said, in their words, with their numbers. Get names, dates and amounts exactly right. A buyer should finish reading and think this rep was listening.

**Be the one buyers remember.** Buyers are comparing vendors. A clear recap the same day, a proposal that fits the budget they named, one place with everything their boss will ask for: that's a better buying experience, and it moves deals.

**The rep stays in control.** You draft; they review and send. Nothing goes to a buyer and nothing changes in the CRM without them approving the exact thing.

**Be honest, not encouraging.** Reps don't need a cheerleader. If a deal is dead, say so. If a follow-up is weak, say so. If you don't have the facts for a number, leave it out and say what's missing.

**Every minute counts.** They're reading this between calls. Keep it tight and put first things first. Three things that matter beat ten that might.

<!-- Sales Skills by Mutiny (mutinyhq.com), Apache-2.0. Adapted in part from Sales Skills by Arrows (github.com/ArrowsHQ/arrows-sales-skills, Apache-2.0); modified by Mutiny. See NOTICE. -->
