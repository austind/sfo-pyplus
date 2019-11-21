#!/usr/bin/env python

import yaml
from pprint import pprint as pp

with open('serialization1.yml') as f:
    pp(yaml.safe_load(f))
