#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

def save_config(host, cfg):
    with open(f"{host}.cfg", "w") as f:
        f.write(cfg)

def get_config(conn):
    if conn.device_type == 'cisco_ios':
        cmd = 'show run'
    if conn.device_type == 'juniper_junos':
        cmd = 'show conf'
    return conn.send_command(cmd)

devices = {
    'cisco3': {
        'device_type': 'cisco_ios',
        'host': 'cisco3.lasthop.io',
        'username': 'pyclass',
        'password': password,
    },
    'srx2': {
        'device_type': 'juniper_junos',
        'host': 'srx2.lasthop.io',
        'username': 'pyclass',
        'password': password,
    },
}

for device in devices.values():
    with ConnectHandler(**device) as conn:
        print(conn.send_command('show version'))
        cfg = get_config(conn)
        save_config(conn.host, cfg)

