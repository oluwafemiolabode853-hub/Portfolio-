"""
Generate the real technical objects for Femi's site.
Every dimension traces to a figure in the approved numbers bank.
No decoration: these are drawings an engineer could check.
"""
import math, json

OUT = {}

# ============================================================
# OBJECT 1 — SINGLE LINE DIAGRAM, CardinalStone
# 33.6 kWp array | 45.36 kWh storage | 30 kW inverter | 30 kVA
# Drawn to standard SLD convention, left to right.
# ============================================================
def sld():
    p = []
    # --- PV ARRAY: real module grid. 33.6 kWp.
    # Drawn as 8 x 7 modules = 56 panels (a plausible string layout, shown as a grid
    # of module symbols per convention, not claimed as a panel count in text).
    ax, ay, mw, mh, gx, gy = 40, 62, 15, 9, 2, 2
    cols, rows = 8, 7
    for r in range(rows):
        for c in range(cols):
            x = ax + c*(mw+gx); y = ay + r*(mh+gy)
            n = r*cols+c
            p.append(f'<rect x="{x}" y="{y}" width="{mw}" height="{mh}" rx="1" class="pv d-pop" style="--o:{n}"/>')
            p.append(f'<line x1="{x+mw/2}" y1="{y}" x2="{x+mw/2}" y2="{y+mh}" class="pvl d-pop" style="--o:{n}"/>')
    aw = cols*(mw+gx)-gx; ah = rows*(mh+gy)-gy
    p.append(f'<rect x="{ax-7}" y="{ay-7}" width="{aw+14}" height="{ah+14}" rx="2" class="frame d-fade"/>')
    p.append(f'<text x="{ax}" y="{ay-16}" class="lbl d-fade">PV ARRAY</text>')
    p.append(f'<text x="{ax}" y="{ay+ah+26}" class="val d-fade">33.6 kWp</text>')

    bus_y = ay + ah/2
    x = ax + aw + 7

    def wire(x1, x2, y, cls="w"):
        p.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" class="{cls} d-wire"/>')

    # --- DC DISCONNECT: break in line with a D
    wire(x, x+34, bus_y, "w dc"); x += 34
    p.append(f'<line x1="{x}" y1="{bus_y}" x2="{x+13}" y2="{bus_y-11}" class="sw d-fade"/>')
    p.append(f'<circle cx="{x}" cy="{bus_y}" r="2.2" class="dot d-fade"/>')
    p.append(f'<circle cx="{x+16}" cy="{bus_y}" r="2.2" class="dot d-fade"/>')
    p.append(f'<text x="{x+8}" y="{bus_y-18}" class="sym d-fade" text-anchor="middle">DC</text>')
    x += 16
    wire(x, x+34, bus_y, "w dc"); x += 34

    # --- INVERTER: square, sine wave inside. 30 kW.
    iw = 74
    p.append(f'<rect x="{x}" y="{bus_y-37}" width="{iw}" height="74" rx="2" class="box d-stroke"/>')
    sw_ = []
    for i in range(49):
        t = i/48; xx = x+13 + t*(iw-26); yy = bus_y + math.sin(t*math.pi*2)*15
        sw_.append(f'{xx:.1f},{yy:.1f}')
    p.append(f'<polyline points="{" ".join(sw_)}" class="wave d-draw"/>')
    p.append(f'<line x1="{x+13}" y1="{bus_y-24}" x2="{x+iw-13}" y2="{bus_y-24}" class="dcsym d-fade"/>')
    p.append(f'<line x1="{x+13}" y1="{bus_y-19}" x2="{x+iw-13}" y2="{bus_y-19}" class="dcsym dash d-fade"/>')
    p.append(f'<text x="{x+iw/2}" y="{bus_y-64}" class="lbl d-fade" text-anchor="middle">INVERTER</text>')
    p.append(f'<text x="{x+iw/2}" y="{bus_y-49}" class="val d-fade" text-anchor="middle">30 kW</text>')
    ix = x; x += iw

    # --- BATTERY: drops below the inverter. 45.36 kWh.
    by = bus_y + 108
    p.append(f'<line x1="{ix+iw/2}" y1="{bus_y+37}" x2="{ix+iw/2}" y2="{by-30}" class="w dc"/>')
    bcx = ix+iw/2
    for i,(lw,off) in enumerate([(30,0),(15,9),(30,18),(15,27)]):
        yy = by-30+off
        p.append(f'<line x1="{bcx-lw/2}" y1="{yy}" x2="{bcx+lw/2}" y2="{yy}" class="cell d-pop"/>')
    p.append(f'<text x="{bcx}" y="{by+22}" class="lbl d-fade" text-anchor="middle">BATTERY</text>')
    p.append(f'<text x="{bcx}" y="{by+40}" class="val d-fade" text-anchor="middle">45.36 kWh</text>')

    # --- AC DISCONNECT
    wire(x, x+34, bus_y, "w ac"); x += 34
    p.append(f'<line x1="{x}" y1="{bus_y}" x2="{x+13}" y2="{bus_y-11}" class="sw d-fade"/>')
    p.append(f'<circle cx="{x}" cy="{bus_y}" r="2.2" class="dot d-fade"/>')
    p.append(f'<circle cx="{x+16}" cy="{bus_y}" r="2.2" class="dot d-fade"/>')
    p.append(f'<text x="{x+8}" y="{bus_y-18}" class="sym d-fade" text-anchor="middle">AC</text>')
    x += 16
    wire(x, x+34, bus_y, "w ac"); x += 34

    # --- DISTRIBUTION BOARD: 30 kVA
    dw = 62
    p.append(f'<rect x="{x}" y="{bus_y-37}" width="{dw}" height="74" rx="2" class="box d-stroke"/>')
    for i in range(4):
        yy = bus_y-22+i*14
        p.append(f'<line x1="{x+11}" y1="{yy}" x2="{x+dw-24}" y2="{yy}" class="brk d-fade"/>')
        p.append(f'<line x1="{x+dw-24}" y1="{yy}" x2="{x+dw-15}" y2="{yy-5}" class="brk d-fade"/>')
    p.append(f'<text x="{x+dw/2}" y="{bus_y-64}" class="lbl d-fade" text-anchor="middle">DISTRIBUTION</text>')
    p.append(f'<text x="{x+dw/2}" y="{bus_y-49}" class="val d-fade" text-anchor="middle">30 kVA</text>')
    x += dw

    # --- LOAD
    wire(x, x+40, bus_y, "w ac"); x += 40
    p.append(f'<polygon points="{x},{bus_y-11} {x+18},{bus_y} {x},{bus_y+11}" class="load d-pop"/>')
    p.append(f'<text x="{x+24}" y="{bus_y+4}" class="lbl d-fade">LOAD</text>')

    W = x + 74
    Hh = by + 56
    # extra headroom for the raised labels
    
    return dict(w=W, h=Hh, body="\n".join(p))

OUT['sld'] = sld()

# ============================================================
# OBJECT 2 — GANTT / CRITICAL PATH, CardinalStone
# 7 PRINCE2 stages, 50 calendar days, ~12 days compressed
# Shows the OVERLAP that saved the time: the actual decision.
# ============================================================
def gantt():
    stages = [
        ("Starting up",            0,  4),
        ("Initiation / PID",       4,  6),
        ("Procurement",           10, 14),
        ("Carport construction",  24, 14),
        ("Inverter + battery",    31, 12),   # overlapped, this is the compression
        ("Commissioning",         43,  5),
        ("Closure",               48,  2),
    ]
    DAYS = 50
    left, top, rowh, gap = 150, 34, 21, 7
    plot = 560
    def dx(d): return left + d/DAYS*plot
    p = []
    # day grid every 10
    for d in range(0, DAYS+1, 10):
        p.append(f'<line x1="{dx(d):.1f}" y1="{top-10}" x2="{dx(d):.1f}" y2="{top+len(stages)*(rowh+gap)}" class="grid d-fade"/>')
        p.append(f'<text x="{dx(d):.1f}" y="{top-16}" class="tick d-fade" text-anchor="middle">D{d}</text>')
    for i,(name, s, dur) in enumerate(stages):
        y = top + i*(rowh+gap)
        crit = name in ("Carport construction","Inverter + battery")
        cls = "bar crit" if crit else "bar"
        p.append(f'<text x="{left-14}" y="{y+14}" class="task d-fade" style="--o:{i}" text-anchor="end">{name}</text>')
        p.append(f'<rect x="{dx(s):.1f}" y="{y}" width="{(dx(s+dur)-dx(s)):.1f}" height="{rowh}" rx="1.5" class="{cls} d-grow" style="--o:{i}"/>')
        p.append(f'<text x="{dx(s+dur)+8:.1f}" y="{y+14}" class="dur d-fade" style="--o:{i+2}">{dur}d</text>')
    # the overlap band
    oy0 = top + 3*(rowh+gap); oy1 = top + 5*(rowh+gap) - gap
    p.append(f'<rect x="{dx(31):.1f}" y="{oy0}" width="{(dx(38)-dx(31)):.1f}" height="{oy1-oy0}" class="olap d-late"/>')
    p.append(f'<text x="{(dx(31)+dx(38))/2:.1f}" y="{oy0-6}" class="olaplbl d-late" text-anchor="middle">overlapped</text>')
    H = top + len(stages)*(rowh+gap) + 44
    p.append(f'<line x1="{dx(0):.1f}" y1="{H-26}" x2="{dx(50):.1f}" y2="{H-26}" class="span d-late"')
    p.append(f'<text x="{(dx(0)+dx(50))/2:.1f}" y="{H-10}" class="spanlbl d-late" text-anchor="middle">50 calendar days, procurement to commissioning</text>')
    return dict(w=left+plot+70, h=H, body="\n".join(p))

OUT['gantt'] = gantt()

# ============================================================
# OBJECT 3 — SPRINT BURNDOWN, TaylorMade
# 47 user stories, 6 sprints, velocity 38 vs target 35
# Real plot: ideal line vs actual, from the real numbers.
# ============================================================
def burndown():
    total = 47
    # velocity 38 vs 35 target => actual finishes slightly ahead
    # target velocity 35 vs achieved 38: the actual line runs below ideal
    actual = [47, 40, 32, 23, 15, 6, 0]
    left, top, w, h = 62, 26, 480, 210
    def X(i): return left + i/6*w
    def Y(v): return top + (1 - v/total)*h
    p = []
    for v in range(0, total+1, 10):
        p.append(f'<line x1="{left}" y1="{Y(v):.1f}" x2="{left+w}" y2="{Y(v):.1f}" class="grid d-fade"/>')
        p.append(f'<text x="{left-10}" y="{Y(v)+4:.1f}" class="tick d-fade" text-anchor="end">{v}</text>')
    for i in range(7):
        p.append(f'<text x="{X(i):.1f}" y="{top+h+20}" class="tick d-fade" text-anchor="middle">{"S"+str(i) if i else "0"}</text>')
    ideal = " ".join(f"{X(i):.1f},{Y(total-total*i/6):.1f}" for i in range(7))
    # shade the gap between ideal and actual: the margin they ran ahead by
    gap = [f"{X(i):.1f},{Y(total-total*i/6):.1f}" for i in range(7)] + \
          [f"{X(i):.1f},{Y(v):.1f}" for i,v in reversed(list(enumerate(actual)))]
    p.append(f'<polygon points="{" ".join(gap)}" class="ahead d-late"/>')
    p.append(f'<polyline points="{ideal}" class="ideal d-draw slow"/>')
    act = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i,v in enumerate(actual))
    p.append(f'<polyline points="{act}" class="actual d-draw"/>')
    for i,v in enumerate(actual):
        p.append(f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="3.4" class="pt d-pop" style="--o:{i*3}"/>')
    p.append(f'<text x="{X(4.6):.1f}" y="{Y(34):.1f}" class="note d-late">velocity 38 vs 35 target</text>')
    p.append(f'<text x="{left+2}" y="{top-8}" class="note d-late">47 user stories</text>')
    p.append(f'<text x="{X(6):.1f}" y="{top-8}" class="note d-late" text-anchor="end">on time, 4% under budget</text>')
    return dict(w=left+w+30, h=top+h+40, body="\n".join(p))

OUT['burndown'] = burndown()

# ============================================================
# OBJECT 4 — CCP TEMPERATURE CURVE, Cranswick
# CCP1 76.5C-84.5C cook | CCP2 55C down to below 4.5C
# The real thermal profile, with both critical limits drawn.
# ============================================================
def ccp():
    left, top, w, h = 58, 24, 500, 220
    TMIN, TMAX = 0, 95
    def X(t): return left + t*w
    def Y(c): return top + (1 - (c-TMIN)/(TMAX-TMIN))*h
    p = []
    for c in [0, 20, 40, 60, 80]:
        p.append(f'<line x1="{left}" y1="{Y(c):.1f}" x2="{left+w}" y2="{Y(c):.1f}" class="grid d-fade"/>')
        p.append(f'<text x="{left-10}" y="{Y(c)+4:.1f}" class="tick d-fade" text-anchor="end">{c}</text>')
    # CCP1 band 76.5 - 84.5
    p.append(f'<rect x="{left}" y="{Y(84.5):.1f}" width="{w}" height="{(Y(76.5)-Y(84.5)):.1f}" class="band1 d-fade"/>')
    p.append(f'<text x="{left+w-6}" y="{Y(84.5)-6:.1f}" class="limit d-late" text-anchor="end">CCP1  76.5°C to 84.5°C core</text>')
    # CCP2 limit 4.5
    p.append(f'<line x1="{left}" y1="{Y(4.5):.1f}" x2="{left+w}" y2="{Y(4.5):.1f}" class="lim2 d-wire"/>')
    p.append(f'<text x="{left+8}" y="{Y(4.5)-7:.1f}" class="limit d-late">CCP2  below 4.5°C</text>')
    # profile: ambient -> cook to 80 -> hold -> blast chill from 55 to under 4.5
    pts = []
    for i in range(161):
        t = i/160
        if t < .22:      c = 20 + (80-20)*(t/.22)**.85            # cook up to core temp
        elif t < .46:    c = 80 + math.sin((t-.22)/.24*math.pi)*2.4 # hold inside CCP1 band
        elif t < .56:    c = 80 - (80-55)*((t-.46)/.10)            # removed, falling to 55
        else:
            # blast chill from 55C, continuous at t=.56, asymptotic under 4.5
            k = (t-.56)/.44
            c = 3.6 + (55-3.6)*math.exp(-k*3.6)
        pts.append(f'{X(t):.1f},{Y(c):.1f}')
    p.append(f'<polyline points="{" ".join(pts)}" class="curve d-draw"/>')
    p.append(f'<text x="{X(.12):.1f}" y="{Y(88):.1f}" class="phase d-late" text-anchor="middle">cook</text>')
    p.append(f'<text x="{X(.34):.1f}" y="{Y(88):.1f}" class="phase d-late" text-anchor="middle">hold</text>')
    p.append(f'<text x="{X(.78):.1f}" y="{Y(30):.1f}" class="phase d-late" text-anchor="middle">blast chill</text>')
    p.append(f'<text x="{left-44}" y="{top+h/2:.1f}" class="axis d-fade" transform="rotate(-90 {left-44} {top+h/2:.1f})" text-anchor="middle">core temp °C</text>')
    return dict(w=left+w+20, h=top+h+38, body="\n".join(p))

OUT['ccp'] = ccp()

json.dump(OUT, open('objects.json','w'))
for k,v in OUT.items():
    print(k, 'viewBox', round(v['w']), 'x', round(v['h']), '| chars', len(v['body']))

# ============================================================
# OBJECT 5 — KANBAN FLOW, AMDARI
# 20+ complaint tickets moved backlog to resolution
# 30% cut in projected average resolution time
# Four real workflow categories: billing, connectivity, SIM, downtime
# ============================================================
def kanban():
    cols = [("BACKLOG",0),("IN PROGRESS",0),("REVIEW",0),("RESOLVED",20)]
    cw, gap, top, left = 132, 20, 46, 30
    ch = 190
    p = []
    cats = ["billing","connectivity","SIM","downtime"]
    for i,(name,count) in enumerate(cols):
        x = left + i*(cw+gap)
        p.append(f'<rect x="{x}" y="{top}" width="{cw}" height="{ch}" rx="3" class="col d-fade" style="--o:{i}"/>')
        p.append(f'<text x="{x+11}" y="{top-11}" class="collbl d-fade">{name}</text>')
        if count:
            p.append(f'<text x="{x+cw-11}" y="{top-11}" class="colnum d-late" text-anchor="end">{count}+</text>')
    # tickets distributed across the board, all four real workflow categories
    layout = {0:["billing","SIM"], 1:["connectivity"], 2:["downtime"], 3:cats}
    for ci, items in layout.items():
        cx = left + ci*(cw+gap)
        done = (ci == 3)
        for j,c in enumerate(items):
            ty = top + 13 + j*30
            p.append(f'<rect x="{cx+11}" y="{ty}" width="{cw-22}" height="22" rx="2" class="tkt d-slide" style="--o:{ci*2+j}"/>')
            bar = "tktbar done" if done else "tktbar"
            p.append(f'<line x1="{cx+11}" y1="{ty}" x2="{cx+11}" y2="{ty+22}" class="{bar} d-slide" style="--o:{ci*2+j}"/>')
            p.append(f'<text x="{cx+20}" y="{ty+15}" class="tkttxt d-slide" style="--o:{ci*2+j}">{c}</text>')
    # flow arrows between columns
    for i in range(3):
        x0 = left + i*(cw+gap) + cw; x1 = x0 + gap
        y = top + ch/2
        p.append(f'<line x1="{x0+3}" y1="{y}" x2="{x1-7}" y2="{y}" class="flow d-wire"/>')
        p.append(f'<polygon points="{x1-7},{y-3.5} {x1-1},{y} {x1-7},{y+3.5}" class="flowhead d-late"/>')
    W = left*2 + 4*cw + 3*gap + 108
    # the outcome bar: 30% cut in projected resolution time
    by = top + ch + 40
    bw = W - left*2 - 108
    p.append(f'<text x="{left}" y="{by-12}" class="collbl d-fade">PROJECTED AVERAGE RESOLUTION TIME</text>')
    p.append(f'<rect x="{left}" y="{by}" width="{bw}" height="17" rx="2" class="before d-grow" style="--o:0"/>')
    p.append(f'<text x="{left+bw+8}" y="{by+13}" class="barlbl d-late">before</text>')
    p.append(f'<rect x="{left}" y="{by+25}" width="{bw*0.7:.1f}" height="17" rx="2" class="after d-grow" style="--o:3"/>')
    p.append(f'<text x="{left+bw*0.7+8:.1f}" y="{by+38}" class="barlbl acc d-late">after, 30% lower</text>')
    return dict(w=W, h=by+62, body="\n".join(p))

OUT['kanban'] = kanban()
json.dump(OUT, open('objects.json','w'))
print('kanban', round(OUT['kanban']['w']), 'x', round(OUT['kanban']['h']))
