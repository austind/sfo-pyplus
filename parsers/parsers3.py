#!/usr/bin/env python

import os
from getpass import getpass
from netmiko import ConnectHandler
from pprint import pprint as pp

password = os.environ.get('NET_PASS') or getpass()

args = {
    'device_type': 'arista_eos',
    'host': 'arista1.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'global_delay_factor': 1,
}

with ConnectHandler(**args) as conn:
    pp(conn.send_command('show ip route', use_textfsm=True))
