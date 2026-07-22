#!/usr/bin/env python3
"""Export the 19-term define/build/Qantas set as a Quizlet import file.

Output: Operations-ER-Quizlet.txt — one card per line, TAB between the term
side and the definition side. In Quizlet: Create > Study set > Import,
paste the file contents, set "Between term and definition" = Tab and
"Between cards" = New line.
"""
import html
import re

from build_anki_er_drills import TERMS


def plain(s):
    s = re.sub(r'<li>', ' • ', s)
    s = re.sub(r'</li>', '', s)
    s = re.sub(r'<ol>|</ol>|<ul>|</ul>', ' ', s)
    s = re.sub(r'<br\s*/?>', ' ', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    s = s.replace('\t', ' ')
    return re.sub(r'\s+', ' ', s).strip()


rows = []
for term, (definition, build, qantas) in TERMS.items():
    rows.append((f'DEFINE: {term}', plain(definition)))
    rows.append((f'BUILD (characteristics & features): {term}', plain(build)))
    rows.append((f'QANTAS evidence: {term}', plain(qantas)))

with open('Operations-ER-Quizlet.txt', 'w') as f:
    for front, back in rows:
        f.write(f'{front}\t{back}\n')

print(f'Wrote Operations-ER-Quizlet.txt with {len(rows)} cards')
