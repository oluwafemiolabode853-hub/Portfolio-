"""
Write the five drawings from build_objects.py into index.html.

index.html is the page. This script only replaces what sits inside each
<svg class="obj"> element (and its viewBox), so the copy, the portrait and
everything else on the page are left exactly as they are.

    python3 build_site.py
"""
import re
from pathlib import Path
from build_objects import build

PAGE = Path(__file__).with_name('index.html')

# every <svg class="obj"> on the page, in document order:
# the hero ghost, then FILE 01 to FILE 05
ORDER = ['sld', 'sld', 'gantt', 'burndown', 'ccp', 'kanban']

SVG = re.compile(r'(<svg class="obj" viewBox=")[^"]*("[^>]*>\n).*?(\n</svg>)', re.S)

def main():
    obj = build()
    html = PAGE.read_text(encoding='utf-8')
    found = len(SVG.findall(html))
    if found != len(ORDER):
        raise SystemExit(f'expected {len(ORDER)} drawings in index.html, found {found}')
    keys = iter(ORDER)
    def put(m):
        o = obj[next(keys)]
        return f"{m.group(1)}0 0 {round(o['w'])} {round(o['h'])}{m.group(2)}{o['body']}{m.group(3)}"
    out = SVG.sub(put, html)
    PAGE.write_text(out, encoding='utf-8')
    print('index.html', 'updated' if out != html else 'already up to date')

if __name__ == '__main__':
    main()
