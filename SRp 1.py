import sys
import json

argentina = {}
chile = {}
for line in sys.stdin:
    strana, land, ploran, name = line.rstrip('\n').split('#')
    if strana == 'A':
        if land not in argentina:
            argentina[land] = []
        argentina[land].append((ploran, name))
    if strana == 'Ch':
        if land not in chile:
            chile[land] = []
        chile[land].append((ploran, name))
for el in argentina:
    an = []
    pl = []
    for i in argentina[el]:
        if i[0] == 'animal':
            an.append(i[1])
        else:
            pl.append(i[1])
    res = sorted(an) + sorted(pl)
    argentina[el] = res
for el in chile:
    an = []
    pl = []
    for i in chile[el]:
        if i[0] == 'animal':
            an.append(i[1])
        else:
            pl.append(i[1])
    res = sorted(an) + sorted(pl)
    chile[el] = res

js = {'argentina': argentina, 'chile': chile}

with open('patagonia.json', 'w') as f:
    json.dump(js, f)
