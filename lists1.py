#!/usr/bin/env python

items = [
    'one',
    'two',
    'three',
    'four',
    'five',
]

items.append('six')
items.append('seven')

first = items.pop(0)
print(len(items))
items.sort()
