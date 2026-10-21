# Oluwafemi Olabode — Delivery Record

Five projects drawn as the instruments they were delivered with.
Static site: no build step, no dependencies, no framework.

    index.html          markup and content (the portrait is embedded in it)
    style.css           design system, drawing ink, all animation
    script.js           path measurement, scroll observers, theme, pause, progress
    build_objects.py    generates the five SVG drawings from real specifications
    build_site.py       writes those drawings into index.html
    assets/             portrait originals (PNG fallback for very old browsers)

Open index.html. That is the whole workflow.

## Putting it on GitHub Pages

1. Unzip the download first. GitHub does not unzip files for you.
2. In the repository, choose Add file, then Upload files.
3. Open the unzipped folder, select everything inside it (including the
   assets folder) and drag it onto the upload page. Dragging keeps folders;
   the "choose your files" button does not.
4. Commit. Under Settings, then Pages, set the source to the main branch,
   root folder. The site appears at https://USERNAME.github.io/REPOSITORY/

The page only strictly needs index.html, style.css and script.js. The
portrait is embedded in index.html, so it still shows if assets/ is missing.

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

**Pause.** The button beside the theme switch stops every layer and shows
every element in its finished state. The choice is remembered on that
browser. Verified: 0 running animations and 0 hidden elements while paused,
and 0 hidden elements with JavaScript disabled.

Motion is on by default even when the computer's system setting asks for
reduced motion. Many Windows laptops have that setting on (Settings,
Accessibility, Visual effects, "Animation effects" off), and following it left
the page completely still on laptops while it animated on phones. To follow
the system setting again instead, add this line to the small script in the
head of index.html:
`if(matchMedia("(prefers-reduced-motion: reduce)").matches&&!localStorage.getItem("oo-motion"))d.className+=" reduced";`

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

    python3 build_site.py       # writes all five drawings into index.html

build_site.py replaces only what is inside each drawing's svg element, so
the copy and the rest of the page are untouched. Running it on an unchanged
build_objects.py leaves index.html byte for byte the same.
(python3 build_objects.py on its own writes objects.json, for inspection.)

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
carries an aria-label, every drawing parses as well formed SVG, visible
keyboard focus, works with JavaScript disabled, all motion can be paused, no
horizontal overflow from 360px to 2560px, prints cleanly, zero console errors.

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
