
from pprint import pprint as pp
import json

with open('struct_data1.json') as f:
    routing_table = json.load(f)

pp(routing_table)

print(type(routing_table))
print()
print(len(routing_table))
print()
print(type(routing_table[0]))
print()
print(len(routing_table[0]))
print()

parsed_data = {}

for entry in routing_table:
   if entry['protocol'] != 'L':
        network = entry['network']
        parsed_data[network] = {
            'nexthop_if': entry['nexthop_if'],
            'nexthop_ip': entry['nexthop_ip'],
        }

pp(parsed_data)
