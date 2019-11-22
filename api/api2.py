#!/usr/bin/env python

import os
import requests
from pprint import pprint as pp


TOKEN = os.environ['NETBOX_TOKEN']
BASE_URL = "https://netbox.lasthop.io/api"
HEADERS = {
    "accept": "application/json; version=2.4;",
    "authorization": f"Token {TOKEN}",
}
response = requests.get(f"{BASE_URL}/dcim/devices", headers=HEADERS, verify=False)

pp(response.json())
