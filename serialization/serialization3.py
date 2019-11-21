#!/usr/bin/env python

import yaml
import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint as pp

with open('serialization3.yml') as f:
    devices = yaml.safe_load(f)

password = os.environ.get('NET_PASS') or getpass()

for device in devices.values():
    device['password'] = password
    with ConnectHandler(**device) as conn:
        pp(conn.send_command('show ip interface brief', use_textfsm=True))

