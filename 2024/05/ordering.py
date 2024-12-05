import sys


def create_mapping(rules):
    output = {}
    for rule in rules:
        first, second = rule.split("|")
        first = int(first)
        second = int(second)
        values = output.get(first, [])
        values.append(second)
        output[first] = values
    return output


if __name__ == "__main__":
    filename = sys.argv[1]

    with open(filename) as f:
        data = f.readlines()

    rules = [x.strip() for x in data if "|" in x]
    updates = [x.strip() for x in data if "|" not in x]

    mappings = create_mapping(rules)
    print(mappings)
