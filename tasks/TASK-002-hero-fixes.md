# TASK-002 — GeetAI start (home) page visual fixes

Repo: geetai-studio-website. File: `index.html` (and `geetai.html` is a copy — apply same fix to both).
Owner: Aniket (non-coder). Test locally with `python3 -m http.server 8080`, view at 1440px AND 380px.
Use Opus 4.8. List nothing — just fix these 4, then commit + push, then I redeploy.

## The 4 problems (from screenshots of the live hero)

### 1. Hero headline text is CUT OFF on the right
- The H1 "Your AI OS<br>For <animated word>" (around `index.html:1101`, CSS `.hero h1` at `:274`).
- The rotating word (WORDS array at `:2094`: 'Sales Automation', 'Lead Generation', etc.) overflows the
  right edge and gets clipped (e.g. "For Sales Auto…").
- FIX: make the heading container not clip — allow the longest word ('Content Creation' / 'Sales Automation')
  to fit fully. Reduce font-size with `clamp()` so it scales, set the animated word span to `white-space:nowrap`
  but inside a container with enough width / `overflow:visible`, and reserve min-width so layout doesn't jump.
  Must look correct on desktop AND mobile (380px) — no horizontal scroll, no cut letters.

### 2. Background rotating shape is blank / clipped
- `#galaxy-logo` (CSS `:302-307`, has `transform: rotate()`). Behind the hero a square/diagram is meant to
  rotate but renders blank and cut off.
- FIX: either make it render correctly (proper SVG/image, centered, not clipped by parent `overflow:hidden`),
  or if the asset is missing/broken, replace with a clean subtle rotating ring/orbit that is fully visible
  and centered behind the hero. It should look intentional, not a cut fragment.

### 3. Floating glass cards: no gap + too small
- The 4 floating cards (Workflow Automation, Digital Product Store, Revenue Analytics, Enterprise Security)
  — markup near `index.html:1389`, CSS `.glass-float-section` / `.glass-float-grid` at `:431-433`.
- FIX: add clear spacing/gap between the 4 cards so they don't touch/overlap, and increase their size
  (roughly 20-30% bigger). Keep them readable and not overflowing on mobile.

### 4. Logo missing / cut
- Nav logo: `.nav-logo-mark img` at `:217` uses `filter:brightness(0) invert(1)` — logo not visible / shows
  only partial "Gee".
- FIX: make the logo display fully and correctly (check the image path/size, the filter may be hiding it,
  the container may be clipping it). Logo must be clearly visible in the top-left on load.

## Rules
- Apply to BOTH index.html and geetai.html (identical files).
- After: update PROJECT_STATUS.md, commit "TASK-002: hero visual fixes", push.
- Don't touch tool pages or other sections.
