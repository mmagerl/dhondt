#!/usr/bin/python3
from collections import defaultdict

default_name = 'ABCDEFGHIJKLMNOPQRSTUVZ'

Ns = int(input('Unesi broj stranaka: '))
Nm = int(input('Unesi broj mandata: '))

table = []

for i in range(Ns):
    line = input('> ').strip()
    parts = line.split(' ')
    if len(parts) == 1:
        # dodijeli ime
        name = default_name[i]
        votes = float(parts[0])
    else:
        name = parts[0]
        votes = float(parts[1])

    for j in range(1, Nm):
        table.append([name, votes / j])


electors = sorted(table, key=lambda x: -x[1])[:Nm]

d = defaultdict(int)
for e in electors:
    d[e[0]] += 1

print()
print(sorted(d.items(), key=lambda x: -x[1]))





