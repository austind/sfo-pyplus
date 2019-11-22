import os
from getpass import getpass
from napalm import get_network_driver
from pprint import pprint as pp

username = os.environ.get('NET_USER') or input('Username: ')
password = os.environ.get('NET_PASS') or getpass()

hosts = ['cisco3', 'cisco4']

config = "ip route 1.1.254.254 255.255.255.255 1.2.3.4"

for host in hosts:
    driver = get_network_driver('ios')
    device = driver(
        hostname=f"{host}.lasthop.io",
        username=username,
        password=password,
    )
    device.open()
    device.load_merge_candidate(config=config)
    pp(device.compare_config())
    print()
    device.discard_config()
    pp(device.compare_config())
    print()
    device.load_merge_candidate(config=config)
    pp(device.compare_config())
    print()
    device.commit_config()
