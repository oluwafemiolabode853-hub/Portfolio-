# Oluwafemi Olabode — Delivery Record

Five projects drawn as the instruments they were delivered with.
Static site: no build step, no dependencies, no framework.

    index.html          markup and content
    style.css           design system, drawing ink, all animation
    script.js           path measurement, scroll observers, theme, progress
    build_objects.py    generates the five SVG drawings from real specifications
    build_site.py       assembles the case-file sections
    assets/             portrait

Open index.html. That is the whole workflow.

## Motion, in three layers

**Layer 1 — assembly on scroll.** Each drawing builds itself as it enters view,
and the whole build lands in about one second so it completes while you are
looking at it. Elements carry a class describing how they appear:

    d-draw    stroked along its length (conductors, plotted curves)
    d-wire    same, faster (short runs, limit lines)
    d-stroke  outlines of boxes and enclosures
    d-pop     scales in (solar modules, data points, battery cells)
    d-grow    scales along X (schedule bars, resolution-time bars)
    d-slide   slides in from the left (Kanban tickets)
    d-fade    fades (labels, grids, ticks)
    d-late    fades last (annotations, callouts)

script.js measures every stroked path with getTotalLength() and writes it to a
--len custom property, so a short wire and a long curve draw at the same speed
rather than the same duration.

**Layer 2 — the structure moves too.** File numbers slide in, headings rise,
spec rows deal in one after another like a table being filled, tags pop in
sequence, the caption's accent rule draws downward, the plate lifts into place,
the timeline's spine draws down its full height with each dot popping as you
pass, credential rows and tool chips stagger, contact buttons rise together.

**Layer 3 — the system stays live.** Because this is a working system it never
freezes into a still image. Around 73 animations run continuously: 56 solar
panels breathe in a staggered sweep, 6 conductors carry flowing current, the
inverter wave pulses, battery cells glow, the Gantt's overlap band and the
resolution-time bar breathe, the availability dot pulses, the section caret
blinks.

Every layer is suspended under prefers-reduced-motion, where all elements are
shown immediately and fully. Verified: 0 infinite animations and 0 hidden
elements remain when reduced motion is requested, and 0 hidden elements with
JavaScript disabled.

## The drawings

  FILE 01  Single line diagram    33.6 kWp array, 45.36 kWh storage, 30 kW
                                  inverter, 30 kVA distribution. Standard SLD
                                  convention, DC and AC disconnects in place.
  FILE 02  Gantt / critical path  7 PRINCE2 stages across 50 calendar days.
                                  Orange bars are the two overlapped stages;
                                  the pulsing band is the ~12 days it saved.
  FILE 03  Sprint burndown        47 stories over 6 sprints. The shaded margin
                                  is velocity 38 running ahead of a 35 target.
  FILE 04  CCP temperature curve  Cook into the 76.5-84.5°C CCP1 band, hold,
                                  blast chill below the 4.5°C CCP2 limit.
  FILE 05  Kanban + resolution    Four real workflows and the 30% fall in
                                  projected average resolution time.

## Regenerating the drawings

    python3 build_objects.py    # writes objects.json
    python3 build_site.py       # rebuilds the case-file sections

Every dimension in build_objects.py traces to a figure in the approved numbers
bank. Change a figure there, not in the HTML. Colours come from CSS custom
properties, so drawings follow light and dark themes automatically.

## Type and colour

IBM Plex Sans / Mono / Serif — commissioned by IBM for technical documentation.
Copper (#C2410C light, #F97316 dark) for live conductors and the critical path;
blue (#0369A1 / #38BDF8) for the AC side and the CCP2 limit. A faint drafting
grid sits under the whole page.

## Verified

WCAG AA contrast (5.49:1 minimum), single h1, no heading skips, every drawing
carries an aria-label, visible keyboard focus, works with JavaScript disabled,
honours prefers-reduced-motion completely, no horizontal overflow from 360px to
2560px, prints cleanly, zero console errors.

## Content rules observed

No invented facts, no salary, no visa or right-to-work detail, no claimed
permanent PM job title, no "Certified Scrum Master" claim, no personal
circumstances. Every figure from the approved numbers bank. UK spelling, no
em dashes.

## Outstanding before it goes public

- Support Worker employer name (the record currently says "London" only)
- Confirmation of the 400/300 student figures (deliberately omitted)
- Optional: one candid working photo would strengthen the record section.
  The single headshot is sufficient as it stands.
