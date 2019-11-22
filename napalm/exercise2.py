import os
from getpass import getpass
from napalm import get_network_driver
from pprint import pprint as pp

username = os.environ.get('NET_USER') or input('Username: ')
password = os.environ.get('NET_PASS') or getpass()

hosts = ['nxos1', 'nxos2']

for host in hosts:
    driver = get_network_driver('nxos')
    device = driver(
        hostname=f"{host}.lasthop.io",
        username=username,
        password=password,
        optional_args={'port': 8443},
    )
    device.open()
    pp(device.get_lldp_neighbors())
