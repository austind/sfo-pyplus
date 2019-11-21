#!/usr/bin/env python

ip_addr = input("IP address: ")
octets = ip_addr.split(".")
print("{:12}{:12}{:12}{:12}".format(*octets))
