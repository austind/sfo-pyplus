#!/usr/bin/env python

device = {
    'ip': '10.2.3.4',
    'username': 'adecoup',
    'password': 't0ps3cret',
    'vendor': 'aruba',
    'model': 'C9500',
}

for k, v in device.items():
    print(f"{k}: {v}")

device['password'] = 'sup3rs3cure'
device['secret'] = 'omgh1dden'
print(device.get('device_type', False))
