#!/usr/bin/env python

ip_addr = input("IP address: ")
octets = ip_addr.split(".")
new_list = octets
new_list[-1] = '0'
for o in octets:
    print(o)
for o in octets:
    print(bin(int(o)))


