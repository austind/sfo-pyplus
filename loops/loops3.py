#!/usr/bin/env python

with open('show_version.txt') as f:
    sh_ver = f.readlines()

for line in sh_ver:
    if 'board ID' in line:
       print(line.split()[-1]) 
