---
name: mutiny-deal-room
description: "Mutiny deal room, from Sales Skills by Mutiny. Builds one customer-ready page for a deal's whole buying group: an executive summary, what we heard in the buyer's words, why us, pricing if it's been discussed, security and legal documents, a shared plan with owners and dates on both sides, who's involved, and resources. Built from every call and email on the deal, in the seller's own brand, so a stakeholder who missed the calls can catch up in two minutes. Rebuild it after each call to keep it current. Nothing is invented and nothing is sent. Use whenever someone says 'Build the Mutiny deal room for [company]', 'build a deal room for [company]', 'update the deal room for [company]', 'I need one place for everything on this deal', 'make a mutual action plan for [company]', or has a deal with several stakeholders who need the same picture."
---


One page the buyer can pass around: everything agreed so far and what happens next. It replaces the long email thread nobody new wants to read.

| Section | What's in it |
|---|---|
| Summary | Why they're looking, what's proposed, where things stand |
| What we heard | Their goals and requirements, in their words |
| Why us | The 2–3 reasons that matter for this buyer, with proof |
| Pricing | Only if pricing has been shared with this buyer |
| Security and legal | Real documents and where each review stands |
| Plan | Who does what by when, on both sides, ending in the decision |
| People | Who's involved, on both sides |
| Resources | Recaps, decks and docs already shared |

## What goes on the page

`kind` is "Deal room". `preparedFor` is the buyer's main contact; add "and team" when several people are involved. Sections, in this order (the page builds a menu from each section's `nav`):

1. **Summary** (`nav`: "Summary"). The title is the outcome they're after. Three `bullets`: why they're looking, what's proposed, where things stand today. A `next` block is not used here; it goes in Plan.
2. **What we heard** (`nav`: "What we heard"). `quotes` (2–4) from across the calls, each with name and date, then `bullets` for requirements and must-haves. Include what different stakeholders care about: security's requirement next to finance's.
3. **Why us** (`nav`: "Why [seller]"). `bullets`: the 2–3 reasons that answer what this buyer asked for, each tied to something they said. Then a `proof` block with 1–2 customer stories from `## Brand and proof`. Never name a competitor.
4. **Pricing** (`nav`: "Pricing"). Only if pricing was shared with this buyer. An `options` block with exactly what was sent or said, not a new offer. If a pricing proposal was built earlier, use its numbers. No pricing shared yet: leave the section out.
5. **Security and legal** (`nav`: "Security"). A `links` block of real documents with real URLs (security overview, compliance report request page, MSA, DPA) from the seller's website or what was already sent, each with a `note` on status ("sent Oct 3", "in review with IT"). Only documents you found. None found: leave the section out and say so under Check before sending.
6. **Plan** (`nav`: "Next steps"). A `plan` block: every step from now to the decision, each with an owner by name (theirs or the seller's) and a date. Mark what's done as "done" and the one upcoming step as "next". Include only steps someone agreed to or the buyer described as their process; a step you're proposing gets "(proposed)" in `what`. End with one `next` block.
7. **People** (`nav`: "People"). Two `people` blocks: the buyer's team, then the seller's. For each buyer, `role` is what they do in this decision in plain words ("reviews security", "signs off on budget"), only as they or a colleague described it.
8. **Resources** (`nav`: "Resources"). A `links` block: call recaps, the deck, the demo recording, the proposal. Real links only.

Title: what they're trying to achieve, with both names if it reads well ("Same-day follow-ups for every Vantage rep"). Under 12 words.

**Keeping it current.** A deal room is rebuilt, not written once. When asked to update it:
- Read the previous version if it's in this conversation or the project, and everything on the deal since.
- Move finished steps to "done," set the new "next," add new people, add what was newly said or sent.
- In the chat message, list what changed in three lines or fewer, so the person can tell the buyer what's new.

{{ASSET_GUIDE}}

## Special cases

- **Early deal, one or two calls:** Summary, What we heard, Plan and People are enough. Say which sections are waiting on what.
- **Something said in confidence:** if a buyer shared something about a colleague, internal politics or another vendor, leave it out. The whole buying group reads this page.
- **Stakeholders disagree:** show each requirement with who raised it. Don't pick a side on the page; flag it to the person in the chat message.
- **The buyer described their buying process:** use their steps and their names for them in Plan.
- **Leader building for a rep's deal:** `preparedBy` is the rep who owns the deal.

## Page template

```html
{{ASSET_TEMPLATE}}
```
