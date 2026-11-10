---
name: mutiny-pricing-proposal
description: "Mutiny pricing proposal, from Sales Skills by Mutiny. Builds a customer-ready pricing page for one deal from the call where the buyer shared their budget and requirements: what we heard in their words, one or two options inside the range they named, what's included, the rollout plan, terms and the next step. In the seller's own brand, written so the buyer can forward it to finance. Prices come only from the person's pricing, CRM or what was said to this buyer; nothing is invented and nothing is sent. Use whenever someone says 'Build the Mutiny pricing proposal for [company]', 'build a pricing proposal for [company]', 'put together pricing options for [company]', 'turn that pricing call into a proposal', or needs a quote, pricing options or a proposal a buyer asked for after a call."
---


A pricing proposal the buyer can open, understand in a minute and forward to whoever signs. Built from what they said on the call, not from a blank template.

| Section | What's in it |
|---|---|
| What we heard | Their goal, budget, must-haves and timing, in their words |
| Your options | One or two options inside the range they gave, with what each includes |
| Rollout | How they get from signature to live, with dates if discussed |
| The cost of waiting | Only when the buyer gave the numbers for it |
| Terms and next step | Billing, term, what's included in both, and the one next step with a date and who signs |

## What goes on the page

`kind` is "Pricing proposal". Sections, in this order:

1. **What we heard.** `quotes` (1–3, the buyer's words on the goal, the budget and the must-haves, with name and date), then `bullets` for the requirements the options have to meet. The title says what they're trying to do ("60 engineers shipping on [Product] by January").
2. **Your options.** One `options` block.
   - **Two options when the buyer gave a range or a ceiling:** one that matches the budget they named, one under their ceiling that adds what they said they wanted most. Mark one `pick: true` and say why in its `fit` line, using their reason, not yours.
   - **One option** when they gave a single number, asked for one quote, or the person's `## My rules` says they send one.
   - **Never an option above a ceiling the buyer stated.** If the person's pricing can't fit the range, stop and tell the person before building anything.
   - `price` and `per` exactly as the person presents pricing ("$70,000", "per year · 60 seats"). `includes` lists 3–6 items, with every must-have the buyer named shown in both options.
   - Use the option names from `## Pricing and packaging`. If the person's real tiers are named, use those names.
3. **Rollout.** A `steps` block of 2–4 stages, only from what was discussed or what `mutiny-sales-process.md` says normally happens after signature. Dates only if someone said them.
4. **The cost of waiting.** Include only when the buyer gave the inputs (hours, headcount, churn, revenue). A `math` block that shows the calculation, with the source of each number in the `note`. No inputs from the buyer: leave the section out.
5. **Terms and next step.** `bullets` for billing, term length and anything included in both options, then one `next` block: what happens, when, and who signs off ("Exec review on Oct 9 · Rob Kim signs off").

Title: the outcome plus the fit ("Two options for 60 seats, both inside your budget"). Under 12 words.

{{ASSET_GUIDE}}

## Special cases

- **No budget or requirements on any call:** don't guess a range. Say what's missing and offer the question to ask ("What range are you working with?"), or build a one-option proposal at list price if the person asks for that.
- **The buyer asked for a discount:** include it only if the person tells you the figure, or the CRM or an email shows it was offered. Otherwise show list price and put "discount asked for, not shown" under Check before sending.
- **A proposal was already sent:** read it first. Build on its numbers, and say in the chat message what changed.
- **Procurement or legal asked for specific terms:** list them under Terms as "requested," not as agreed, unless an email shows the seller agreed.
- **Leader building for a rep's deal:** `preparedBy` is the rep who owns the deal.

## Page template

```html
{{ASSET_TEMPLATE}}
```
