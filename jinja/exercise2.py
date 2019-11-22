from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

def main():
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader(".")
   
    devices = {
        'nxos1': {
            'interface': 'Ethernet2/1',
            'ip_address': '10.1.100.1',
            'netmask': '24',
        },
        'nxos2': {
            'interface': 'Ethernet2/1',
            'ip_address': '10.1.100.2',
            'netmask': '24',
        }
    }

    template = 'exercise2.j2'

    for host, j2_vars in devices.items():
        t = env.get_template(template)
        output = t.render(**j2_vars)
        print("-" * 42)
        print(host)
        print("-" * 42)
        print(output)

if __name__ == "__main__":
    main()
