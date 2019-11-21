#!/usr/bin/env python

from pprint import pprint as pp
import re

def read_file(file_name):
    with open(file_name) as f:
        return f.read()

def get_vendor(show_ver):
    pattern = r"^(\w+)\s"
    match = re.search(pattern, show_ver)
    if match:
        return match.group(1)

def get_model(show_ver):
    pattern = r"^(.*?) processor.*?bytes of memory\."
    match = re.search(pattern, show_ver, flags=re.M)
    if match:
        return match.group(1)

def get_os_version(show_ver):
    pattern = r"^.*Version (\S+),"
    match = re.search(pattern, show_ver, flags=re.M)
    if match:
        return match.group(1)

def get_serial(show_ver):
    pattern = r"board ID (\w+)"
    match = re.search(pattern, show_ver)
    if match:
        return match.group(1)

def get_uptime(show_ver):
    pattern = r"^.* uptime is (.+)$"
    match = re.search(pattern, show_ver, flags=re.M)
    if match:
        return match.group(1) 

show_ver = read_file('show_version.txt')
result = {
    'vendor': get_vendor(show_ver),
    'model': get_model(show_ver),
    'os_version': get_os_version(show_ver),
    'serial': get_serial(show_ver),
    'uptime': get_uptime(show_ver),
}
pp(result)
