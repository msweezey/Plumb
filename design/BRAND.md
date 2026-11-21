# Plumb brand guide

**Plumb** is an AI-native analyst firm. It measures how brands show up where shopping is going (AI answers, search, media and agent checkout) and publishes the results as the **Plumb Index**.

> **Know what good looks like.**

This guide covers the current *hybrid* direction: the editorial warmth of Option 1 (serif name mark, purple) with the measuring-instrument precision of Option 3 (white page, level green, rulers and gauges). Reference UI: [`ui/hybrid/`](ui/hybrid/). Tokens: [`brand/hybrid/tokens.css`](brand/hybrid/tokens.css).

---

## 1. Name and voice

| | |
|---|---|
| Company | Plumb |
| Product | The Plumb Index (category editions, e.g. *The Agentic Commerce Index · Beauty*) |
| Tagline | Know what good looks like. |
| Hero line | Know where you stand. |
| Primary CTA | Get your brand's rank · Measure me → |

**Why "Plumb":** a plumb line shows true vertical. To *plumb* something is to measure its depth. The brand is the measurement, not the opinion.

**Voice.** Plain, specific, measured.
- Lead with the number, then the meaning: *"Top-2 spender, but AI names it in only 6% of beauty prompts."*
- Short sentences. No hype words (revolutionary, unlock, supercharge).
- Say how a score is measured beside the score, every time.
- Use names, not euphemisms: *Bought vs earned*, *Pass / Partial / Fail*.
- Mark sample data clearly: *Illustrative · not real scores*.

## 2. Logo

![Plumb wordmark](brand/hybrid/logos/plumb-wordmark.svg)

**Name mark.** "Plumb" set in **Instrument Serif**, regular, tracking −2%, ink `#17131F`, followed by a small **purple dot** (`#6A2BE0`) on the baseline. (In the SVG files the dot is a purple full stop, so it lands correctly whatever the rendered width.) The dot is the plumb bob: the point the line settles on.

- Dot diameter ≈ 18% of cap height (8px at 40px type, 7px at 34px). Keep it small. It is a full stop, not a bullet.
- Dot gap: 2px at 40px.
- One colour of dot only: purple on white, `#9B6BFF` on dark.
- Don't add a symbol, arrow or underline to the name mark. Don't set it in bold or italic. Don't recolour the word.

![Plumb Index lockup](brand/hybrid/logos/plumb-index-lockup.svg)

**Index lockup.** "Plumb **Index**": "Index" in purple, the dot after it. Used at the top of the product sidebar and on reports.

**Report masthead.** "Plumb. *Index*": a purple full stop and italic "Index", used on report covers and email.

Files: [`brand/hybrid/logos/`](brand/hybrid/logos/). The SVGs reference the Instrument Serif web font. Outline the text before you send them to print.

**Clear space:** the height of the "P" on every side. **Minimum size:** 72px wide on screen.

## 3. Colour

Always on a **white page**. Purple is the brand. Green is the measurement. Amber is the warning. Use them for those jobs only.

### Brand
| Token | Hex | Use |
|---|---|---|
| Purple | `#6A2BE0` | Dot, links, active filters, primary buttons, "you" highlight |
| Purple light | `#9B6BFF` | Purple on dark surfaces |
| Lavender | `#ECE4FF` | Active nav item fill |
| Lavender soft | `#F4EFFF` | Your row in a table, target zone on gauges |
| Night | `#1E1238` | Dark CTA panels ("Where do you stand?") |

### Signal
| Token | Hex | Use |
|---|---|---|
| Level green | `#00B862` | **Fills only**: bars, gauge markers. Never text (fails contrast). |
| Level ink | `#00754A` | Green text: rank #1, "Earned", "Pass" |
| Level wash | `#E8F8EF` | Pass badge background |
| Amber | `#A35400` | Warning text: "Bought", "Fail" |
| Amber wash | `#FBEFE3` | Fail badge background |

### Neutrals
| Token | Hex | Use |
|---|---|---|
| Ink | `#17131F` | Headlines, body |
| Ink cool | `#0F1411` | Numbers and table data |
| Lead | `#625C70` | Secondary text, labels |
| Hairline | `#EFECF5` | Borders, dividers |
| Tick | `#D9D3E6` | Ruler and gauge tick marks |
| Mist | `#F7F5FB` | Table headers, segmented controls |
| Paper | `#FFFFFF` | Background |

## 4. Typography

| Role | Typeface | Setting |
|---|---|---|
| Display: name mark, section headlines | **Instrument Serif** | 400, −2% tracking, 1.0 line height. Italic for one emphasised word: *"Where do* ***you*** *stand?"* |
| Headings: brand names, card titles | **Inter Tight** | 600, −2% tracking |
| Body and UI | **Geist** (Inter as fallback) | 400 / 500 / 600; body 15–19px |
| Labels: kickers, column headers | **Geist Mono** | 500, 11px, UPPERCASE, +10% tracking, Lead colour |
| Data: ranks, percentages | **JetBrains Mono** | 500, tabular |

All are free on Google Fonts.

Rule of thumb: **serif for the voice, sans for the interface, mono for the measurement.**

## 5. Graphic language: the instrument

Plumb looks like a measuring tool, not a dashboard.

- **Ruler.** A hairline tick ruler (minor ticks every 8px, major every 40px) sits under section headings and marks a new section.
- **Gauges.** Rounded tracks with tick marks, a purple target zone (*what good looks like*) and a dot marker for where a brand sits.
- **Bars.** Thin 6px rounded bars for share metrics. Ink for most bars, level green for AI answer share.
- **Rank numbers** are set in mono. #1 is in level ink.
- **"You" row.** Lavender-soft fill, a 3px purple left edge, and a purple "YOU" tag in mono.
- No radar charts, drop shadows (beyond a soft card lift), gradients or stock photography.

## 6. Components

| Component | Spec |
|---|---|
| Primary button | Purple fill, white text, 12px radius, 56px tall in CTAs / 44px in UI |
| Secondary button | White, hairline border, ink text, 10px radius |
| Ink button | `#17131F` fill, white text |
| Segmented tabs | Mist pill track; active tab is white with a hairline ring, 600 weight |
| Filter chip | 8px radius, mono micro-label + value; active = 1.5px purple border, purple text |
| Card | White, hairline border, 16px radius |
| Section panel | 24px radius; dark Night panel for the benchmark CTA, white with hairline for the report signup |
| Badge | Pill; Pass = level wash/level ink, Partial = mist/ink, Fail = amber wash/amber |
| Sidebar nav | 12px radius items; active = lavender fill, purple 600 text |

Radii: 8 inputs · 10–12 buttons · 16 cards · 24 panels · pill for chips and badges.

## 7. Layout

- Max content width **1360px**, 40px side gutters, 80px between sections.
- Sections run: hero → Index (sidebar + table) → *Where do you stand?* benchmark → *Get the Index in your inbox* report signup → plans → footer.
- Every data view shows its source and method next to it: data built for people *and* AI to read and cite.
- Tables use real `<table>` markup with captions. Labels are visible or screen-reader-only, never placeholder-only.

## 8. Data honesty

- Every score shows how it is measured (e.g. *AI answer share: share of ~200 category prompts that name the brand, across 4 AI engines*).
- Proxies are labelled: *Share of spend: active ads and new creatives (proxy until spend is licensed)*.
- Mockups that use real brand names carry **"Illustrative · not real scores"**.

---

*Earlier directions, kept for reference: [Option 1 purple](brand/option-1-purple/), [Option 2 editorial](brand/option-2-editorial/), [Option 3 instrument](brand/option-3-instrument/).*
