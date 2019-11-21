#!/usr/bin/env python

with open('source.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line)

with open('dest.txt', 'w') as f:
    f.write('line1\n')
    f.write('line2\n')
    f.write('line3\n')

with open('dest.txt', 'a') as f:
    f.write('line4\n')

