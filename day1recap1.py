#!/usr/bin/env python

with open('day1exercise1-in.txt') as f:
    sh_bgp = f.read().splitlines()

# Strip header
sh_bgp = sh_bgp[8:]

with open('day1exercise1-out.txt', 'w') as f:
    for line in sh_bgp:
        fields = line.split()
        prefix = fields[1]
        as_path = " ".join(fields[5:-1])
        f.write(f"Prefix: {prefix} AS Path: {as_path}\n")
