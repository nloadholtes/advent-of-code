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

def is_order_correct(mappings, update):
    for page in update:
        pass
    return True

if __name__ == "__main__":
    filename = sys.argv[1]

    with open(filename) as f:
        data = f.readlines()

    rules = [x.strip() for x in data if "|" in x]
    updates = [list(map(lambda y: int(y), x.strip().split(","))) for x in data if x != "\n" and "|" not in x]

    mappings = create_mapping(rules)
    print(mappings)
    middle_pages = []
    for update in updates:
        if is_order_correct(mappings, update):
            middle_page = int(len(update)/2)
            middle_pages.append(update[middle_page])
    print(f"Sum of middle pages: {sum(middle_pages)}")

