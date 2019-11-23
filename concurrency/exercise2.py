from concurrent.futures import ThreadPoolExecutor, as_completed
import os
from getpass import getpass
from netmiko import ConnectHandler

USERNAME = os.environ.get("NET_USER") or input("Username: ")
PASSWORD = os.environ.get("NET_PASS") or getpass()

devices = [
    {"host": "cisco3.lasthop.io", "device_type": "cisco_ios"},
    {"host": "cisco4.lasthop.io", "device_type": "cisco_ios"},
    {"host": "arista1.lasthop.io", "device_type": "arista_eos"},
    {"host": "arista2.lasthop.io", "device_type": "arista_eos"},
]


def show_command(dev, cmd):
    conn = ConnectHandler(**dev)
    output = conn.send_command(cmd)
    conn.disconnect()
    return output


def main():
    pool = ThreadPoolExecutor(max_workers=8)
    threads = []
    for dev in devices:
        dev["username"] = USERNAME
        dev["password"] = PASSWORD
        threads.append(pool.submit(show_command, dev, "show ip arp"))

    for thread in as_completed(threads):
        print()
        print(thread.result())
        print()


if __name__ == "__main__":
    main()
