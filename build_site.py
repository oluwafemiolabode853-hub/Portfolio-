import json
OBJ = json.load(open('_objects_html.json'))

HEAD = '''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Oluwafemi Olabode · Delivery Record</title>
<meta name="description" content="Five projects drawn as the instruments they were delivered with. Oluwafemi Olabode, moving into project management from a decade in electrical engineering, site supervision and technical education. PRINCE2 7 Practitioner. London.">
<meta name="theme-color" content="#0B0E13">
<meta property="og:title" content="Oluwafemi Olabode · Delivery Record">
<meta property="og:description" content="Five projects drawn as the instruments they were delivered with.">
<meta property="og:type" content="profile">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Serif:ital,wght@0,300;1,300&display=swap" rel="stylesheet">
<script>document.documentElement.className+=" js";</script>
<link rel="stylesheet" href="style.css">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Person","name":"Oluwafemi Olabode","email":"oluwafemiolabode853@gmail.com","address":{"@type":"PostalAddress","addressLocality":"London","addressCountry":"GB"},"sameAs":["https://www.linkedin.com/in/oluwafemi-olabode"],"knowsAbout":["Project Management","PRINCE2","Agile Delivery","Solar PV","Battery Energy Storage","Electrical Engineering"]}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

NAV = '''
<header class="bar" id="bar">
  <a class="id" href="#top">
    <span class="id-mark" aria-hidden="true">
      <svg viewBox="0 0 26 26"><rect x="1" y="1" width="24" height="24" rx="2" fill="none" stroke="currentColor"/><path d="M5 18 L10 8 L13 14 L16 6 L21 18" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>
    </span>
    <span class="id-name">Oluwafemi Olabode</span>
  </a>
  <nav class="nav" aria-label="Primary">
    <a href="#f01"><i>01</i> Solar</a>
    <a href="#f02"><i>02</i> Schedule</a>
    <a href="#f03"><i>03</i> Sprints</a>
    <a href="#f04"><i>04</i> Control</a>
    <a href="#f05"><i>05</i> Flow</a>
  </nav>
  <div class="bar-r">
    <button class="tgl" id="tgl" aria-label="Switch colour theme" title="Switch colour theme">
      <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path class="sun" d="M12 4V2m0 20v-2m8-8h2M2 12h2m13.66-5.66l1.41-1.41M4.93 19.07l1.41-1.41m11.32 0l1.41 1.41M4.93 4.93l1.41 1.41M12 8a4 4 0 100 8 4 4 0 000-8z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><path class="moon" d="M20 14.5A8.5 8.5 0 019.5 4a8.5 8.5 0 1010.5 10.5z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
    </button>
    <a class="bar-cta" href="#contact">Contact</a>
    <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mnav"><span></span><span></span></button>
  </div>
</header>
<div class="mnav" id="mnav" hidden>
  <a href="#f01"><i>01</i> Solar array</a>
  <a href="#f02"><i>02</i> Schedule</a>
  <a href="#f03"><i>03</i> Sprints</a>
  <a href="#f04"><i>04</i> Process control</a>
  <a href="#f05"><i>05</i> Ticket flow</a>
  <a href="#record"><i>06</i> Record</a>
  <a href="#contact"><i>07</i> Contact</a>
</div>
<div class="prog" aria-hidden="true"><i id="prog"></i></div>
'''

HERO = '''
<main id="main">
<section class="hero" id="top">
  <div class="hero-in">
    <p class="kick"><span class="dot" aria-hidden="true"></span>London · Available at two weeks notice</p>
    <h1 class="h-big">
      <span class="l"><span class="w">Five</span> <span class="w">projects,</span></span>
      <span class="l"><span class="w">drawn</span> <span class="w">as</span> <span class="w">the</span></span>
      <span class="l"><span class="w">instruments</span> <span class="w em">they</span></span>
      <span class="l"><span class="w em">were</span> <span class="w em">delivered</span> <span class="w em">with.</span></span>
    </h1>
    <div class="hero-b">
      <p class="hero-p">
        I am Femi. A decade in electrical engineering, site supervision and
        technical education, now delivering projects under formal governance.
        PRINCE2&nbsp;7 Practitioner and AgilePM certified.
      </p>
      <p class="hero-p sm">
        Everything below is drawn from the real specification. The array is the
        array. The schedule is the schedule. Nothing here is illustration.
      </p>
    </div>
    <a class="hero-go" href="#f01">
      <span>Open the first file</span>
      <svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M12 4v16m-6-6l6 6 6-6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </a>
  </div>
  <div class="hero-fig" aria-hidden="true">OBJ_SLD_GHOST</div>
</section>
'''

def case(num, anchor, client, role, title, spec, obj, notes, tags, outcome):
    specrows = "\n".join(
        f'<div class="sp"><dt>{k}</dt><dd>{v}</dd></div>' for k,v in spec)
    noteps = "\n".join(f'<p class="rv">{n}</p>' for n in notes)
    tagli = "".join(f'<li>{t}</li>' for t in tags)
    return f'''
<section class="file" id="{anchor}">
  <div class="wrap">
    <header class="fh">
      <div class="fh-l">
        <span class="fnum">FILE {num}</span>
        <h2 class="fh-t rv">{title}</h2>
      </div>
      <dl class="fh-r rv">
        <div class="sp"><dt>Client</dt><dd>{client}</dd></div>
        <div class="sp"><dt>Role</dt><dd>{role}</dd></div>
      </dl>
    </header>

    <figure class="plate">
      <div class="plate-in">{obj}</div>
      <figcaption class="cap">{outcome}</figcaption>
    </figure>

    <div class="fbody">
      <dl class="spec rv">{specrows}</dl>
      <div class="ftext">{noteps}<ul class="tags">{tagli}</ul></div>
    </div>
  </div>
</section>'''

FILES = HERO.replace('OBJ_SLD_GHOST', OBJ['sld'])

FILES += case("01","f01","CardinalStone, Lagos","Project Consultant and Project Engineer",
  "A 30&nbsp;kVA hybrid solar and battery system, commissioned on the planned date",
  [("Array","33.6 kWp"),("Storage","45.36 kWh"),("Inverter","30 kW"),("System","30 kVA"),("Standard","PRINCE2 7 stages")],
  OBJ['sld'],
  ["I ran the full PRINCE2 lifecycle on this system, from procurement start to commissioning in 50 calendar days across seven stages and more than twenty sub&#8209;activities.",
   "I wrote and version controlled the PID, a bill of materials running to more than fifty line items, the installation schedule, the risk register, the quality register and the highlight reports, then handed the full set over at closure. I set up the project board with the client sponsor and ran stage boundary reviews across the procurement, fabrication and installation teams.",
   "Operator and remote monitoring training was delivered at handover."],
  ["PRINCE2","Solar PV","BESS","Hybrid inverter","Commissioning","Handover"],
  "Commissioned on the planned date. No slippage, no exceptions raised.")

FILES += case("02","f02","CardinalStone, Lagos","Schedule and critical path",
  "The two stages I overlapped, and the twelve days it saved",
  [("Duration","50 calendar days"),("Stages","7"),("Sub-activities","20+"),("Compression","~12 days"),("Slippage","None")],
  OBJ['gantt'],
  ["The critical path was the problem. Carport construction and the inverter and battery installation were planned in sequence, which put the commissioning date at risk before procurement had even finished.",
   "I overlapped them. The orange bars above are the two stages, and the dashed band is the seven days they ran together. That compressed the critical path by around twelve days without moving the date the client had been given.",
   "Overlapping stages moves risk from the schedule onto the site, so it is a decision to take deliberately and to hold the quality register against. It held."],
  ["Critical path","Stage gates","Risk register","Highlight reports"],
  "The commissioning date the client was given at initiation is the date it was commissioned.")

FILES += case("03","f03","TaylorMade Fitness App","Project Coordinator, freelance",
  "47 user stories, six sprints, delivered 4% under a fixed price",
  [("Team","3, remote"),("Sprints","6 × 2 weeks"),("Stories","47"),("Velocity","38 vs 35 target"),("Budget","4% under")],
  OBJ['burndown'],
  ["I coordinated a designer, a front end developer and a back end developer through six two&#8209;week sprints to ship an iOS and Android MVP inside a twelve week engagement.",
   "The shaded margin above is the distance the team ran ahead of the ideal line. Average velocity held at 38 story points against a target of 35, across a backlog of 47 stories and a product requirements document covering ten features.",
   "It was a fixed price engagement billed across six milestone invoices, so scope control was the whole job. Twelve risks were tracked to closure, there were twelve sprint review demos and three rounds of user testing with fifteen participants, and it closed with no payment disputes."],
  ["Agile","Backlog","Velocity","Fixed price","UAT","Remote team"],
  "Delivered on time and 4% under budget, with no payment disputes.")

FILES += case("04","f04","Cranswick Country Foods plc","Critical Control Point Operative",
  "Two critical limits, and the batch I stopped between them",
  [("CCP1","76.5°C to 84.5°C core"),("CCP2","55°C to below 4.5°C"),("Line","High volume cooked poultry"),("Records","Audit ready, every batch")],
  OBJ['ccp'],
  ["Every batch on this line lives inside the two limits drawn above. The shaded band is CCP1, the core temperature the product must reach and hold. The dashed line at the bottom is CCP2, the temperature it must be chilled below, on a controlled curve, before it can move on.",
   "I operated both, and logged start and finish times and core temperature readings for every batch so that traceability stayed audit ready at all times.",
   "On one cook I noticed product browning ahead of specification part way through. I judged that the process might be running out of specification and stopped it, escalating to the shift supervisor before the batch moved on. Cooker settings and temperatures were rechecked and CCP compliance held.",
   "Raising something awkward early is cheaper than explaining it afterwards. That is the same instinct as an exception report, in a different building."],
  ["HACCP","CCP","Process control","Traceability","Escalation"],
  "Compliance held, because the line stopped before the batch progressed rather than after.")

FILES += case("05","f05","AMDARI","Scrum Master and Agile Project Management",
  "A ticketing system that cut projected resolution time by 30%",
  [("Portfolio","4 projects"),("Countries","3"),("Tickets","20+ to resolution"),("Resolution time","30% lower"),("Governance","8 roles")],
  OBJ['kanban'],
  ["On the telecom workstream there was no single place to see a complaint. I built a centralised Trello Kanban board and moved more than twenty complaint tickets from backlog through to resolution across the four workflows above: billing, connectivity, SIM and downtime.",
   "I mapped those workflows end to end in Draw.io, produced a RAID log flagging SLA breach risks, and turned the findings into a prioritised backlog behind a three week delivery plan. Projected average resolution time fell by 30%.",
   "The board mattered less than the fact that managers could see where everything stood for the first time. Most delivery problems are visibility problems first.",
   "Across the wider portfolio I run sprint planning, stand ups, reviews and retrospectives for teams in Canada, Switzerland and New Zealand, coordinate an eight role programme governance structure on a health systems workstream inside GDPR and Swiss FADP requirements, and led Sprint 1 planning for an ed tech platform serving more than 120,000 learners and 150 institutional partners."],
  ["Scrum","Kanban","RAID","Jira","Confluence","Miro","GDPR"],
  "Managers could see the queue for the first time, and the projected resolution time fell by 30%.")

open('_files.html','w').write(HEAD + NAV + FILES)
print('files written')
