#!/usr/bin/env python


from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device = {
  'device_type': 'cisco_nxos',
  'host': 'nxos2.lasthop.io',
  'username': 'pyclass',
  'password': password,
}

with ConnectHandler(**device) as conn:
    conn.send_config_set(['logging console 3'])
    conn.save_config()

