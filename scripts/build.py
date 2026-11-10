#!/usr/bin/env python3
"""Assembles every SKILL.md from src/.

Each skill = src/skills/<name>.md (its own instructions)
           + src/shared-context.md (appended to every skill)
with these placeholders filled in:
  {{REPORT_TEMPLATE}}  -> src/templates/<name>.html   (daily brief, meeting prep)
  {{ASSET_GUIDE}}      -> src/asset-guide.md           (pricing proposal, business case, deal room)
  {{ASSET_TEMPLATE}}   -> src/templates/asset.html

Output goes to <name>/SKILL.md (plain files, any AI tool) and
plugins/mutiny-sales-skills/skills/<name>/SKILL.md (the Claude plugin).
Edit files in src/, then run:  python3 scripts/build.py
"""
import pathlib, re, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
PLUGIN = ROOT / "plugins" / "mutiny-sales-skills"
ORDER = ["mutiny-setup", "mutiny-daily-brief", "mutiny-meeting-prep", "mutiny-follow-up", "mutiny-check-in",
         "mutiny-pricing-proposal", "mutiny-business-case", "mutiny-deal-room"]
NOTICE = ("<!-- Sales Skills by Mutiny (mutinyhq.com), Apache-2.0. Adapted in part from Sales Skills by Arrows "
          "(github.com/ArrowsHQ/arrows-sales-skills, Apache-2.0); modified by Mutiny. See NOTICE. -->")

def main():
    shared = (SRC / "shared-context.md").read_text().strip()
    guide = (SRC / "asset-guide.md").read_text().strip()
    asset = (SRC / "templates" / "asset.html").read_text().strip()
    errors = []
    for name in ORDER:
        body = (SRC / "skills" / f"{name}.md").read_text().strip()
        tpl = SRC / "templates" / f"{name}.html"
        if "{{REPORT_TEMPLATE}}" in body:
            body = body.replace("{{REPORT_TEMPLATE}}", tpl.read_text().strip())
        body = body.replace("{{ASSET_GUIDE}}", guide).replace("{{ASSET_TEMPLATE}}", asset)
        out = f"{body}\n\n---\n\n{shared}\n\n{NOTICE}\n"
        m = re.match(r'---\nname: ([a-z0-9-]+)\ndescription: "(.*)"\n---\n', out)
        if not m: errors.append(f"{name}: bad frontmatter")
        elif m.group(1) != name: errors.append(f"{name}: name mismatch")
        elif len(m.group(2)) > 1024: errors.append(f"{name}: description is {len(m.group(2))} chars (max 1024)")
        if "{{" in out: errors.append(f"{name}: unfilled placeholder")
        for dest in (ROOT / name, PLUGIN / "skills" / name):
            dest.mkdir(parents=True, exist_ok=True)
            (dest / "SKILL.md").write_text(out)
        print(f"built {name:26s} {len(out):6d} chars")
    for f in ("LICENSE", "NOTICE"):
        shutil.copy(ROOT / f, PLUGIN / f)
    if errors:
        print("\n".join(errors)); sys.exit(1)

if __name__ == "__main__":
    main()
