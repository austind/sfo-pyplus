#!/usr/bin/env python

names = [
    'Amelia',
    'Alexi',
    'Annalyse',
]

name4 = input("Name: ")

names.append(name4)

print("{:>10}{:>10}{:>10}{:>10}".format(*names))
print(f"{names[0]:>10}{names[1]:>10}{names[2]:>10}{names[3]:>10}")
