import yaml
import os
from napalm import get_network_driver
from pprint import pprint as pp
from getpass import getpass
from exercise1_devices import devices as nxos

username = os.environ.get('NET_USER') or input('Username: ')
password = os.environ.get('NET_PASS') or getpass()

with open('exercise1.yml') as f:
    eos = yaml.load(f)

for args in nxos:
    driver = get_network_driver(args.pop('driver'))
    args['username'] = username
    args['password'] = password
    args['optional_args'] = {
        'port': 8443
    }
    device = driver(**args)
    device.open()
    facts = device.get_facts()
    pp(facts['model'])

for host, args in eos.items():
    driver = get_network_driver(args.pop('driver'))
    args['username'] = username
    args['password'] = password
    device = driver(**args)
    device.open()
    facts = device.get_facts()
    pp(facts['model'])

