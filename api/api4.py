#!/usr/bin/env python

import json
import os
import requests
from pprint import pprint as pp

TOKEN = os.environ['NETBOX_TOKEN']
BASE_URL = "https://netbox.lasthop.io/api"
HEADERS = {
    "Content-Type": "application/json; version=2.4;",
    "authorization": f"Token {TOKEN}",
}

address_id = 110

response = requests.get(f"{BASE_URL}/ipam/ip-addresses/{address_id}/", headers=HEADERS, verify=False)

pp(response.json())

data = {'description': 'El Barto was here', 'address': '192.0.2.254/32'}
response = requests.put(f"{BASE_URL}/ipam/ip-addresses/{address_id}/", data=json.dumps(data), headers=HEADERS, verify=False)

pp(response.status_code)
pp(response.json())

response = requests.delete(f"{BASE_URL}/ipam/ip-addresses/{address_id}/", headers=HEADERS, verify=False)

pp(response.status_code)
