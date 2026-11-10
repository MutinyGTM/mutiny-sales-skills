# Sales Skills by Mutiny

**Free Claude skills for sales. Follow-ups that sound like you, and customer-ready pages built from your calls.**

Turn the AI you already have into a sales assistant that knows your deals and writes like you. These skills learn your voice from your own emails and calls, then do the work around every meeting: the prep, the follow-up, the CRM update, the check-in on a quiet deal, and the pricing proposal, business case or deal room the buyer asked for.

Built by the team at [Mutiny](https://www.mutinyhq.com), the sales assistant built for customer-facing work. This repo is a Claude plugin marketplace, and the same skills are here as plain files that work in ChatGPT, Copilot, Gemini or any other AI tool.

## Quick facts

| | |
|---|---|
| **What it is** | 8 free AI skills for sales reps and sales leaders |
| **Works in** | Claude (plugin or skill upload), ChatGPT, Microsoft Copilot, Google Gemini |
| **Works with** | Any CRM, email, calendar and call recorder your AI tool can connect to. No connection? Paste in a transcript, a CSV export or your notes. |
| **Price** | Free. No signup, no email gate. |
| **License** | Apache 2.0 |
| **Made by** | [Mutiny](https://www.mutinyhq.com) |

---

## Start here: run setup first

Say **"Build my sales profile."** Setup reads your CRM, calls and email, shows you what it learned, asks a couple of quick questions, and saves your sales profile as a few short files: how you write, your sales process, your buyers, pricing, competitors, brand and customer proof, and how you work. Every other skill uses them. Sales leaders also get team files their reps can add, so the whole team follows one process while each rep keeps their own voice.

Setup takes about 5 to 10 minutes. Do it once, and everything Claude drafts sounds like you.

---

## The skills

### Around every meeting

| Skill | Say this | What it does |
|---|---|---|
| **Mutiny setup** (run first) | "Build my sales profile" | Learns your voice, sales process, buyers and brand from your CRM, calls and email. |
| **Mutiny daily brief** | "Run my Mutiny daily brief" | Your day on one screen: what to do first, what changed since yesterday, today's calls, replies waiting, deals at risk. |
| **Mutiny meeting prep** | "Run the Mutiny meeting prep for [company]" | A 60-second brief for one call: who's on it, what they want, what's owed, what you still don't know, what to push for. |
| **Mutiny follow-up** | "Run my Mutiny follow-up" | Right after a call: the follow-up email in your voice and the CRM update from what was said. Nothing is sent or saved until you approve it. |
| **Mutiny check-in** | "Run the Mutiny check-in on [company]" or "...on my pipeline" | Finds deals going quiet and drafts one short, specific check-in per deal. Never "just checking in." |

### Customer-ready pages, built from your calls

| Skill | Say this | What it does |
|---|---|---|
| **Mutiny pricing proposal** | "Build the Mutiny pricing proposal for [company]" | One or two options inside the budget the buyer named, what's included, rollout, terms and the next step. |
| **Mutiny business case** | "Build the Mutiny business case for [company]" | What your champion takes to their exec: current state, what it costs, the future state, benefits with the math shown, and proof. |
| **Mutiny deal room** | "Build the Mutiny deal room for [company]" | One page for the whole buying group: summary, what we heard, why you, pricing, security docs, a shared plan and resources. |

Pages are built in your brand, not ours, from what the buyer said. Prices come only from your own pricing; customer stories only from your own website. See [`examples/`](examples) for sample output.

---

## How the skills work together

Run setup once. Every morning, run your daily brief. Before a call, run meeting prep. Right after it, run follow-up. If the buyer asked for pricing options, something for their exec, or one place for everything, follow-up offers to build it. When a deal goes quiet, run a check-in.

Each skill knows about the others and offers the one next step that makes sense, so you don't have to remember which to run.

---

## Install

### Claude: add the plugin

This repo is a Claude plugin marketplace. Adding the plugin installs all 8 skills at once, and they update when this repo does.

- **Claude (web or desktop):** go to **Customize**, then **Plugins**, then **Add**, then **Add marketplace**, and enter `UncleAchoo/mutiny-sales-skills`. Then add the **Sales Skills by Mutiny** plugin.
- **Claude Code:** run `claude plugin marketplace add UncleAchoo/mutiny-sales-skills`, then `claude plugin install mutiny-sales-skills@mutiny`.

Then start a new chat and type "Build my sales profile."

### Any AI tool: use the files

Each folder at the top of this repo (`mutiny-setup`, `mutiny-daily-brief`, `mutiny-meeting-prep`, `mutiny-follow-up`, `mutiny-check-in`, `mutiny-pricing-proposal`, `mutiny-business-case`, `mutiny-deal-room`) holds one `SKILL.md` file.

1. Open the folder, then the `SKILL.md` file, and download it or copy the raw text.
2. Add it to your AI tool:
   - **Claude:** Settings, then Skills, then Upload.
   - **ChatGPT:** create a Custom GPT and paste the contents into Instructions.
   - **Microsoft Copilot:** create a custom agent and paste it into the instructions.
   - **Google Gemini:** create a Gem and paste it into the Gem instructions.

Start with Mutiny setup, then add the others in any order.

---

## Common questions

### Will it sound like me?

That's the point of setup. It reads the emails you sent to buyers, keeps your greeting, sign-off, length and phrases, and saves real examples by situation. Every draft is written from that file.

### Is my deal data safe?

The skills are instructions, not a pipe to us. Your CRM, email and calls stay connected through your AI tool's own connectors, and the files in this repo don't send anything anywhere. Your sales profile is saved in your own Claude project. Check that your company's AI account is set so your data isn't used for training.

### Will it make things up?

It works from what's in the tools you connect, and every skill is told to leave out anything it can't trace to a call, an email or your CRM. AI can still get things wrong, so read every draft before it goes to a buyer. Nothing is sent for you.

### Does it work with my CRM and call recorder?

Any CRM or recorder your AI tool can connect to. In Claude, check the [connector directory](https://claude.ai/directory). If yours isn't there, paste a transcript or a CSV export and the skills still run.

### What's the catch?

There isn't one. It's free, with no signup, and you can remove it anytime. We build [Mutiny](https://www.mutinyhq.com), a sales assistant that does this without being asked: it takes the notes, drafts the follow-up after every call, and hosts your pages so you can see who opened them. If these skills are useful, Mutiny is free to start.

### Can my whole team use this?

Yes. Each rep adds the plugin and runs setup. A sales leader's setup also makes team files reps can add, so everyone follows the same process in their own voice.

---

## For maintainers

Skills are assembled from `src/`. Edit there, then run `python3 scripts/build.py`. It rebuilds every `SKILL.md` (top-level folders and the plugin copy) and checks the frontmatter. Then raise `version` in `plugins/mutiny-sales-skills/.claude-plugin/plugin.json`. Claude only picks up a change when the version number goes up.

- `src/skills/` — each skill's own instructions
- `src/shared-context.md` — appended to every skill: profile files, sources, the skill list and the Mutiny perspective
- `src/asset-guide.md` — shared by the three page-building skills
- `src/templates/` — the HTML report and page templates

---

## License

Apache 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE). You're free to use, change and share these skills. The license doesn't give rights to the Mutiny name or logo.

Parts of these skills are adapted from [Sales Skills by Arrows](https://github.com/ArrowsHQ/arrows-sales-skills) (Apache 2.0). Thank you to the Arrows team for open-sourcing them.
