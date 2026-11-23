# Content review

Items to confirm or add before publishing. Everything on the site comes from `my_data.md`; nothing was invented.

## Missing information

| Item | Status |
|---|---|
| GitHub URL | Not provided. Button is hidden. Set `CONTACT["github"]` in `data.py`. |
| Public email | Intentionally not published (spam and security). |
| Profile photo | Not provided. Initials and an abstract diagram are used instead. |
| Public résumé PDF | None supplied. The `/resume` page prints to PDF from your browser. |
| Credential IDs and verification links | None provided for any badge or workshop. |
| Badge images | None provided. Initials placeholders are shown. |
| Certification and workshop dates | Not provided, so none are shown. |
| Issuer for the four professional badges | Not stated in `my_data.md`, so no issuer is shown. |
| Project screenshots | None provided. Confidentiality makes this a likely omission anyway. |
| Live site URL (`SITE_URL`) | Needed for canonical links, sitemap and social cards after deployment. |
| Open Graph image | None; social cards use text only. |

## Dates to confirm

- FISDOM: Jan 2022 – Dec 2024 (SDE Trainee Jan 2022 – Nov 2023, SDET – L1 Nov 2023 – Dec 2024), and KPMG from Jan 2025, are taken from your message. `my_data.md` itself only says "January 2022–2025".
- Years of experience are now calculated from `career_start` (`2022-01`) in `data.py` and the visitor's date (for example "nearly 5 years", "5 years", "5+ years", "5.5 years"). Confirm January 2022 is the right start.
- Mega Star Award dated 16 June 2026: confirm the date and wording.

## Possibly confidential

These names appear because they are in your source text. Decide whether each is acceptable to publish:

- Workstream and client names: **PODS**, **KDR**, **META**, and "KPMG Workbench".
- Project names such as ABL Verification, Query Quick, STR Application, META SBX Download Tool.
- Counts: nine US states (ABL), approximately 7,000–8,000 files (META SBX).

## Omitted on purpose

- Matter names under META Matter Support (OPAL, LEVI, NHTSA, Crush AI, Instagram, Threads): possibly client-confidential.
- Phone number or any email address.
- Language proficiency levels (not stated in the source).
- Percentage skill bars; skills are labelled by how they were used instead.

## Ambiguous wording kept as in the source

- Saved Search Modernization and META Matter Support have no technology list in the source, so none is shown and they do not match the skill highlight.
- "Python 2", "TypeScript", "Core Java" and "Shell scripting" are listed as working knowledge because the source lists them without project evidence.
- The source lists "Logging" under two headings; it appears once, as "Logging and error handling".
- BigQuery is listed under both cloud and databases in the source; it appears once, under databases.

## Beyond work section (`BEYOND_WORK` in `data.py`)

- Taken from you: biking (road and adventure trails), video games with Need for Speed: Most Wanted as the favourite, diecast collecting as a new hobby, and exploring places, food and people.
- Written by the assistant from your description, please confirm or edit: the six "friendly go-to person" lines, and small phrases such as "planning the route is half the fun" and "enjoying the small details".
- "Need for Speed: Most Wanted" does not say which release (2005 or 2012); add it if you want it stated.
