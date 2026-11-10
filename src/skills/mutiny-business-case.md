---
name: mutiny-business-case
description: "Mutiny business case, from Sales Skills by Mutiny. Builds a customer-ready executive business case for one deal, for the champion to take to their exec or finance: the current state, what it's costing them, the future state, the benefits with the math shown, what a pilot or rollout has to prove, and customer proof. Built from what the buyer said on calls and in email, in the seller's own brand. Numbers come only from the buyer or the seller's published material; assumptions are labeled; nothing is sent. Use whenever someone says 'Build the Mutiny business case for [company]', 'build a business case for [company]', 'I need an exec summary for their CFO', 'help my champion sell this internally', 'build the ROI case', or needs something a buyer can use to get budget approved."
---


A business case the buyer's champion can forward upstairs and that still makes sense to someone who was never on a call. Six short sections, each with a title that states its point.

| Section | What's in it |
|---|---|
| Current state | What's happening today, sized with the buyer's own numbers |
| What it costs | The consequence in money, time or risk |
| Future state | What changes, as a before and after |
| Benefits | What that's worth, with the math shown, next to the price |
| What has to be true | The capabilities they need and how success will be measured |
| Proof | A customer like them who got the result |

## What goes on the page

`kind` is "Business case". It's written for the person who approves the budget, so `preparedFor` is that person if the buyer named them; otherwise the champion. Sections, in this order:

1. **Current state.** The title is the problem with its size ("About 4,800 hours a year of manual setup slow every new customer"). A `math` block when the buyer gave the inputs (120 customers × 40 hours = 4,800 hours), otherwise `quotes` and `bullets`. Then up to three `bullets` on why act, why this, why now, only from what the buyer said.
2. **What it costs.** The consequence the exec cares about, in their terms: revenue, churn, cost, risk. `metrics` (2–3) or a `compare` block. The source of every number goes in the `note`.
3. **Future state.** One `compare` block, today against the target the buyer said they want. If they never named a target, use `bullets` to describe the change and don't put a number on it.
4. **Benefits.** `metrics` for what the change is worth, with a `math` block showing how you got there. If pricing has been discussed with this buyer, add the price as the last metric so the exec sees value and cost together. If it hasn't, leave price out.
5. **What has to be true.** A `table` with one row per capability the buyer said they need: the capability, how it will be measured, the baseline, the target. This is what a pilot or the first 90 days has to prove. Only criteria the buyer raised or agreed to.
6. **Proof.** One `proof` block with 1–2 customer stories closest to this buyer (industry, size, problem), from `## Brand and proof`. Then one `next` block: the decision or meeting being asked for, with the date.

Title: the result for their business ("Cut time to go live from nine weeks to two"). Under 12 words.

**The numbers rule, in full.** A business case is only as good as its weakest number.
- Use the buyer's figures wherever they gave them, and name who gave them and when in the `note`.
- A benefit that needs a number the buyer didn't give gets a labeled assumption ("Assumes churn falls from 14% to 7%; Lena's stated target, Sep 30 call"). If the assumption is yours and not theirs, say "our assumption" and list it under Check before sending.
- Never present a result from another customer as a forecast for this one. Other customers' results belong in Proof.
- Round honestly, and make sure the arithmetic is right: recompute every `math` block before you show the page.
- If there aren't enough real numbers for sections 2 and 4, build a qualitative case (quotes and bullets), say so in the chat message, and list the two or three numbers to ask the champion for.

{{ASSET_GUIDE}}

## Special cases

- **Early deal, one call so far:** build Current state, Future state and Proof only, and say the rest needs the champion's numbers. Give the questions to ask.
- **The exec has spoken, on a call or in public:** use their stated priorities in section 1, quoted with the source (earnings call, annual report, post). Public sources only when they connect to something the buyer said on a call.
- **The champion will present it:** offer in the chat message to also write three talking points for them.
- **A competitor is in the deal:** the page never names them. Make sure section 5 includes the capabilities where the seller is strongest, if the buyer raised them.
- **Leader building for a rep's deal:** `preparedBy` is the rep who owns the deal.

## Page template

```html
{{ASSET_TEMPLATE}}
```
