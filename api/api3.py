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
data = {"address": "192.0.2.254/32"}
response = requests.post(f"{BASE_URL}/ipam/ip-addresses/", headers=HEADERS, data=json.dumps(data), verify=False)
pp(response.status_code)
pp(response.json())

address_id = response.json()['id']

requests.get(f"{BASE_URL}/ipam/ip-addresses/{address_id}/", headers=HEADERS, verify=False)


pp(response.json())
