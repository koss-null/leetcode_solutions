def solve(a, b):
    return a + b


def get_input(inp):
    a, b = inp.split()
    return int(a), int(b)


def format_output(a):
    return str(a)


def main(a, b):
    return solve(a, b)


if __name__ == "__main__":
    main(*get_input("1 2"))
