#!/usr/bin/env python

import getpass
import re

class NetDevice(object):
    def __init__(self, ip_addr, username, password, serial_number=None, model=None, vendor=None, uptime=None, os_version=None):
        self.show_ver = self.read_file('show_version.txt')
        self.ip_addr = ip_addr
        self.username = username
        self.password = password
        self.serial = self.get_serial(self.show_ver)
        self.model = self.get_model(self.show_ver)
        self.vendor = self.get_vendor(self.show_ver)
        self.uptime = self.get_uptime(self.show_ver)
        self.os_version = self.get_os_version(self.show_ver)

    def read_file(self, file_name):
        with open(file_name) as f:
            return f.read()

    def get_serial(self, show_ver=None):
        pattern = r"board ID (\w+)"
        match = re.search(pattern, show_ver)
        if match:
            return match.group(1)

    def get_model(self, show_ver=None):
        pattern = r"^(.*?) processor.*?bytes of memory\."
        match = re.search(pattern, show_ver, flags=re.M)
        if match:
            return match.group(1)

    def get_vendor(self, show_ver=None):
        pattern = r"^(\w+)\s"
        match = re.search(pattern, show_ver)
        if match:
            return match.group(1)

    def get_uptime(self, show_ver=None):
        pattern = r"^.* uptime is (.+)$"
        match = re.search(pattern, show_ver, flags=re.M)
        if match:
            return match.group(1)

    def get_os_version(self, show_ver=None):
        pattern = r"^.*Version (\S+),"
        match = re.search(pattern, show_ver, flags=re.M)
        if match:
            return match.group(1)


username = getpass.getuser()
password = getpass.getpass()


rtr1 = NetDevice('rtr1', username, password)
rtr2 = NetDevice('rtr2', username, password)
spine01 = NetDevice('spine01', username, password)
leaf01 = NetDevice('leaf01', username, password)

