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
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Daily brief</title>
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
.row.t{grid-template-columns:52px 1fr 14px}
.time{font-weight:700;font-size:13px;color:var(--ink);margin-top:1px}
</style>
</head>
<body>
<div class="wrap" id="app"></div>
<script>
/* Fill in DATA only. Leave everything else as is. */
const DATA = {
  name: "[First name]",
  company: "[Company, for the team view]",
  date: "[Weekday, Month Day]",
  view: "[My day | My day + team · N reps]",
  updated: "[date, time]",
  numbers: { calls: 0, replies: 0, atRisk: 0, changes: 0 },
  doFirst: [],
  sinceYesterday: [],
  atRisk: [],
  closeOut: [],
  calls: [],
  otherMeetings: "",
  replies: [],
  team: [],
  openTime: [],
  howBuilt: "[What was read, any sampling, anything missing]"
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
const item = (mark, title, sub, detail, box0, cls) => {
  const body = `<div class="row${cls ? " " + cls : ""}">${mark}<div>${title}${sub ? `<div class="sub2">${sub}</div>` : ""}</div></div>`;
  const box = box0 || detailBox(detail);
  return box ? `<details class="item"><summary>${body}</summary>${box}</details>` : `<div class="item">${body}</div>`;
};
const quiet = d => d.quietDays == null ? `<span class="tag r">no touch logged</span>` : `<span class="tag ${d.quietDays >= 14 ? "r" : "n"}">${d.quietDays === 0 ? "today" : d.quietDays + "d quiet"}${d.channel ? " · " + esc(d.channel) : ""}</span>`;
const kindMark = k => k === "good" ? `<span class="tick">✓</span>` : `<span class="mark dot ${k === "bad" ? "r" : ""}"></span>`;
const D = DATA, N = D.numbers, team = list(D.team).length > 0;

const go = id => `href="#${id}" onclick="const t=document.getElementById('${id}');if(t){t.scrollIntoView({behavior:'smooth'});}return false;"`;
const cols = items => items.length ? `<div class="cols">${items.join("")}</div>` : "";
const AR = list(D.atRisk), cap = team ? 6 : 5;

let h = "";
h += `<section class="hero"><h1>${team ? esc(D.company || "Sales team") + " daily brief" : esc(D.name) + "'s daily brief"}</h1><p class="sub">${esc([D.date, D.view].filter(Boolean).join(" · "))}</p>`;
h += `<div class="stats num">
  <a class="stat" ${go("calls")}><div class="n">${N.calls}</div><div class="l">Sales calls today</div></a>
  <a class="stat" ${go("replies")}><div class="n">${N.replies}</div><div class="l">Replies waiting</div></a>
  <a class="stat" ${go("at-risk")}><div class="n">${N.atRisk}</div><div class="l"><span class="key r-fill"></span>Deals at risk</div></a>
  <a class="stat" ${go("since")}><div class="n">${N.changes}</div><div class="l">New since yesterday</div></a>
</div></section>`;

h += `<section class="card" id="do-first"><div class="head"><span class="chip">Do first</span><span class="hint">Open any item for the steps</span></div>`;
h += list(D.doFirst).length ? cols(list(D.doFirst).map((t, i) => item(`<span class="num-badge">${i + 1}</span>`, `<span class="title">${esc(t.deal)}</span><span class="who num">${esc([money(t.amount), t.owner].filter(Boolean).join(" · "))}</span><div>${esc(t.action)}</div>`, esc(t.why), null, stepsBox(t.steps, t.context) || detailBox(t.detail) || detailBox(t.why ? [t.why] : [])))) : `<div class="empty">Nothing urgent today.</div>`;
h += `</section>`;

h += `<section class="card" id="since"><div class="head"><span class="chip">New since yesterday</span><span class="hint">Replies, stage moves, wins and losses</span></div>`;
h += list(D.sinceYesterday).length ? cols(list(D.sinceYesterday).map(s => item(kindMark(s.kind), `<span class="title">${esc(s.deal)}</span><span class="who">${esc([money(s.amount), s.owner].filter(Boolean).join(" · "))}</span>`, esc(s.what), s.detail))) : `<div class="empty">Nothing changed since yesterday.</div>`;
h += `</section>`;

h += `<section class="card" id="at-risk"><div class="head"><span class="chip">${team ? "Biggest at risk" : "At risk"}</span><span class="hint">${AR.length > cap || N.atRisk > cap ? `Top ${Math.min(cap, AR.length)} of ${Math.max(N.atRisk, AR.length)}` : ""}</span></div>`;
if (AR.length) {
  h += cols(AR.slice(0, cap).map(d => item(`<span class="mark dot r"></span>`,
    `<span class="title">${esc(d.deal)}</span><span class="who num">${esc([money(d.amount), d.owner, d.stage].filter(Boolean).join(" · "))}</span><div class="qline">${quiet(d)}</div>`,
    `${esc(d.why)}<div class="next">${esc(d.next)}</div>`, d.detail)));
  const rest = AR.slice(cap);
  if (rest.length) h += `<div class="more">${rest.length} more${team ? ", grouped by rep in Team below" : ": " + esc(rest.map(d => d.deal).join(", "))}</div>`;
} else h += `<div class="empty">No deals at risk today.</div>`;
if (list(D.closeOut).length) h += `<div class="more">Close out (${list(D.closeOut).length}, no activity in 60+ days): ${esc(list(D.closeOut).join(", "))}</div>`;
h += `</section>`;

if (team) {
  const repBox = r => {
    const mine = AR.filter(d => d.owner === r.name).map(d => [d.deal, money(d.amount), d.stage].filter(Boolean).join(" · ") + ": " + (d.why || ""));
    return detailBox([...mine, ...(Array.isArray(r.detail) ? r.detail : r.detail ? [r.detail] : [])]);
  };
  h += `<section class="card" id="team"><div class="head"><span class="chip">Team</span><span class="hint">Most at risk first · open a rep for their deals</span></div>`;
  h += list(D.team).map(r => item(`<span class="mark dot ${r.atRiskCount ? "r" : "g"}"></span>`,
    `<div class="rep-row"><div><span class="title">${esc(r.name)}</span><div class="meta num">${r.closingCount || 0} closing this week</div></div><div><span class="sub2">${esc(r.ask)}</span>${r.atRiskCount ? `<span class="tag r">${r.atRiskCount} at risk</span>` : `<span class="tag g">On track</span>`}</div></div>`,
    "", null, repBox(r))).join("");
  h += `</section>`;
}

h += `<section class="card" id="calls"><div class="head"><span class="chip">Today's calls</span><span class="hint">${list(D.calls).length ? list(D.calls).length + " sales calls" : ""}</span></div>`;
h += list(D.calls).length ? list(D.calls).map(c => item(`<span class="time num">${esc(c.time)}</span>`,
  `<span class="title">${esc(c.company)}</span><span class="who">${esc(c.type)}</span><div class="meta">${esc(c.people)}</div><div class="meta num">${esc(c.deal)}</div>`,
  `${esc(c.open)}${c.prep ? `<div class="next">${esc(c.prep)}</div>` : ""}`, c.detail, "", "t")).join("") : `<div class="empty">No sales calls today.</div>`;
if (D.otherMeetings) h += `<div class="more">Also: ${esc(D.otherMeetings)}</div>`;
h += `</section>`;

h += `<section class="card" id="replies"><div class="head"><span class="chip">Replies waiting</span><span class="hint">${list(D.replies).length || ""}</span></div>`;
h += list(D.replies).length ? cols(list(D.replies).map(r => item(`<span class="mark dot ${r.waitingDays >= 2 ? "r" : "y"}"></span>`, `<span class="title">${esc(r.name)}</span><span class="who">${esc([r.company, r.channel].filter(Boolean).join(" · "))}</span>`, `${esc(r.ask)} <span class="tag ${r.waitingDays >= 2 ? "r" : "y"}">${r.waitingDays === 0 ? "today" : r.waitingDays + "d waiting"}</span>`, r.detail))) : `<div class="empty">No buyer is waiting on a reply.</div>`;
h += `</section>`;

h += `<section class="card" id="open-time"><div class="head"><span class="chip">Open time</span></div>`;
h += list(D.openTime).length ? cols(list(D.openTime).map(o => `<div class="item"><div class="row"><span class="mark dot g"></span><div><span class="title num">${esc(o.start)}–${esc(o.end)}</span><span class="who">${esc(o.length)}</span></div></div></div>`)) : `<div class="empty">No open blocks of 30+ minutes.</div>`;
h += `</section>`;

h += `<footer><details><summary>How this report works</summary><div class="about">
<p>This page is rebuilt from the calendar, CRM, email and calls every time it runs. The layout and order never change, so each section is always where it was yesterday. It reads those tools and nothing more: nothing in the CRM, an inbox or a calendar was changed.</p>
<p><b>New since yesterday</b> is buyer replies, stage changes, wins, losses and signed contracts since the start of the last working day. A deal is <b>at risk</b> for one of three reasons: no two-way contact in 14 or more days, no dated next step, or a promised next step that didn't happen. <b>Slipped</b> means the close date has passed and the deal is still open. <b>Close out</b> lists deals with no activity in 60 or more days, to close with a reason or restart. <b>Replies waiting</b> are buyers who wrote last and haven't heard back. <b>Today's calls</b> are sales calls only. Other meetings get one line underneath.</p>
<p>Open the arrow on any row for the details and where they came from.</p>
<p><b>Today:</b> ${esc(D.howBuilt)}</p></div></details><span>Updated ${esc(D.updated)} · Built with Sales Skills by <a href="https://www.mutinyhq.com/?utm_source=sales-skills&utm_medium=report&utm_campaign=daily-brief" target="_blank" rel="noopener">Mutiny</a></span></footer>`;
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
