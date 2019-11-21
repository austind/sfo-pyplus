#!/usr/bin/env python

def read_file(file_name):
    with open(file_name) as f:
        return f.readlines()

def get_serial(show_ver):
    for line in show_ver:
        if 'board ID' in line:
           print(line.split()[-1]) 

get_serial(read_file('show_version.txt'))
