from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment


def main():
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader(".")

    j2_vars = {
        "vrf_name": "blue",
        "rd_number": "100:1",
        "ipv4_af": True,
        "ipv6_af": True,
    }

    print()
    template = "exercise3.j2"
    t = env.get_template(template)
    output = t.render(**j2_vars)
    print(output)
    print()

if __name__ == "__main__":
    main()
