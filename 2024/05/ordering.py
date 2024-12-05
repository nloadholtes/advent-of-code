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
    seen = []
    for page in update:
        seen.append(page)
        values = mappings.get(page, [])  # for pages we don't care about order
        for value in values:
            if value in seen:
                return False
    return True

def reorder(mappings, update):
    output = []
    prev_output = []
    def _process(mappings, update):
        output = []
        for page in update:
            output.append(page)
            values = mappings.get(page, [])
            for value in values:
                if value in output:
                    # reorder? Might need to pop until value fits?
                    last= output.pop()
                    prev = output.pop()
                    output.append(last)
                    output.append(prev)
        print(f"---{output}")
        return output
    output = _process(mappings, update)
    while prev_output != output:
        prev_output = output
        output = _process(mappings, output)
    print(f"{update}\n{output}")
    return output

if __name__ == "__main__":
    filename = sys.argv[1]

    with open(filename) as f:
        data = f.readlines()

    rules = [x.strip() for x in data if "|" in x]
    updates = [list(map(lambda y: int(y), x.strip().split(","))) for x in data if x != "\n" and "|" not in x]

    mappings = create_mapping(rules)
    #print(mappings)
    middle_pages = []
    fixup = []
    for update in updates:
        if is_order_correct(mappings, update):
            middle_page = int(len(update)/2)
            middle_pages.append(update[middle_page])
        else:
            new_row = reorder(mappings, update)
            middle_page = int(len(new_row)/2)
            fixup.append(new_row[middle_page])
            
    print(f"Sum of middle pages: {sum(middle_pages)}")
    print(f"Sum of fixedup pages: {sum(fixup)}")
