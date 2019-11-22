#!/usr/bin/env python

import requests
from pprint import pprint as pp

BASE_URL = 'https://netbox.lasthop.io/api/'
HEADERS = {"accept": "application/json; version=2.4;"}

response = requests.get(BASE_URL, headers=HEADERS, verify=False)
pp(dir(response))
print()
pp(response.text)
print()
pp(response.json())
print()
pp(response.ok)
print()
pp(response.status_code)
print()
