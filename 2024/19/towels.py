import sys


def parse_available(row):
    return set(row.split(","))

def factor(row, available):
    output = []
    # Look for substrings
    for x in range(len(row)):
        pass
    # If there's no martch return false
    return output

if __name__ == "__main__":
    data = [x.strip() for x in open(sys.argv[1]).readlines()]
    available = parse_available(data[0])
    print(available)
    designs = []
    for row in data[2:]:
        needed = factor(row, available)
        if needed != []:
            designs.append(needed)
    print(f"Number of designs we can make: {len(designs)}")
