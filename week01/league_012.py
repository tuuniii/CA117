#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

maxclublen = -1

for line in lines:
    maxclublen = max(maxclublen, len(' '.join(line.strip().split()[1:-8])))

print(f"POS {'CLUB':<{maxclublen}}  P   W   D   L  GF  GA  GD PTS")
for line in lines:
    splitline = line.strip().split()
    p, w, d, l, gf, ga, gd, pts = splitline[-8:]
    pos = splitline[0]
    clubname = ' '.join(line.strip().split()[1:-8])
    print(f"{pos:>3} {clubname:<{maxclublen}} {p:>2} {w:>3} {d:>3} {l:>3} {gf:>3} {ga:>3} {gd:>3} {pts:>3}")
