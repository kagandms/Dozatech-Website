# DOZATECH SEO Foundation Implementation Plan

> **For agentic workers:** The user supplied the complete execution request in the pasted-text attachment; proceed in this session on isolated branch `codex/dozatech-seo-foundation`.

**Goal:** Align DOZATECH’s business copy, technical SEO, CI, and release evidence with the verified business priorities and canonical domain.

**Architecture:** Keep the existing static HTML and Python build pipeline. Centralize domain redirects in Vercel configuration, retain generated route and metadata behavior from `build.py`, and add deterministic checks to the existing verifier. Document the business facts and record external account access separately from public HTTP evidence.

**Tech Stack:** Python 3, static HTML, Vercel JSON configuration, GitHub Actions.

**Spec:** User request pasted in `/Users/kagansmtdms/.codex/attachments/756a6f5c-2735-4279-a17b-a050ce71b5c2/Вставленный текст.txt`.

## Global Constraints

- Primary commercial goal: recurring chemical supply to Istanbul restaurants, hotels, and cafes; pump sales and installation are secondary.
- Machine sales do not imply dishwasher repair; pump maintenance and repair remain offered.
- Approximately 30 years describes technical experience, not company age.
- Main canonical origin is `https://dozatech.com.tr`; redirect rules must preserve path and query and avoid loops.
- Do not change production Vercel settings, DNS, deploy, merge, or remove old hosting projects.
- Preserve baseline measurements and dated work history; do not invent missing business or account facts.

## Review Focus

- Root/www and HTTP/HTTPS redirects preserve the original path/query and converge in one permanent hop.
- Legacy `.html` routes remain permanent and reach the canonical route without a loop.
- Generated HTML, sitemap, robots, social metadata, and structured data use the same canonical origin.
- Form behavior remains testable without delivering a real message; GA4 loader/events remain single-loaded and CSP-permitted.
- CI runs for the actual default branch and pull requests without treating GitHub Pages status as Web CI.

---

### Task 1: Establish repository and release baseline

**Files:** No source edits. Inspect project instructions, Git state, build configuration, public HTTP routes, and available GitHub/Vercel access. Preserve the existing uncommitted roadmap data.

- [ ] Record default branch, base SHA, branch/remote state, and build/test commands.
- [ ] Verify current public HTTP behavior and separate observable facts from account-level facts.
- [ ] Record any unavailable Vercel/GitHub project binding evidence as unverified.

### Task 2: Business context and roadmap

**Files:** Create `docs/business-context.md`; modify `docs/seo-roadmap.md`.

- [ ] Preserve all dated measurements and work-log entries.
- [ ] Add known service boundaries, strengths, target customers, and unknowns without inventing facts.
- [ ] Reorder strategic recommendations so chemical reorder revenue is first and pump sales/installations second.

### Task 3: Canonical URLs and route validation

**Files:** Modify `vercel.json`, `build.py`, and `scripts/verify-build.py` only as needed.

- [ ] Test root/www and HTTP/HTTPS permanent routing, including path/query preservation.
- [ ] Verify old `.html` mappings, canonical outputs, sitemap, robots, social metadata, structured data, key routes, and 404 output.
- [ ] Avoid a redirect loop between Vercel rules and platform domain settings; report required panel configuration without changing it.

### Task 4: Content, contact, and analytics corrections

**Files:** Modify source HTML and corresponding generated `dist` output per repository rules; update `scripts/verify-build.py` for deterministic regressions.

- [ ] Correct copy that implies dishwasher repair or presents technical experience as company age.
- [ ] Retain pump maintenance/repair and dishwasher sales; avoid unsupported superiority, savings, testimonials, or references.
- [ ] Verify WhatsApp/phone destinations, Formspree endpoint and mocked form result/error behavior, GA4 loader count/events, and CSP.

### Task 5: CI and delivery

**Files:** Modify `.github/workflows/main.yml` and any required verifier/configuration.

- [ ] Trigger build/test on push to the actual default branch and on pull requests targeting it.
- [ ] Run existing build and test commands, including checks added for affected behavior.
- [ ] Generate `dist` only according to the existing production rule; inspect final diff.
- [ ] Commit on the isolated branch and prepare an inspectable PR; do not merge, deploy, change DNS, or change production Vercel settings.
