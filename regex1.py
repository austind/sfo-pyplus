#!/usr/bin/env python

import re

with open('regex1.txt') as f:
   sh_int = f.read()

pattern = r'^\s+(\d+) packets (input|output), (\d+) bytes'
match = re.findall(pattern, sh_int, flags=re.M)
if match:
    for item in match:
        packets, direction, data = item
        print(f"Packets {direction}: {packets} Bytes {direction}: {data}")
