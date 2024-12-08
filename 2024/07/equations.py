import sys

def is_valid(row):
    output = False
    value = row[0]
    numbers = row[1]
    total = 1
    for x in numbers:
        total *= x
        if total > value:
            return False

    if total == value:
        output = True

    return output

if __name__ == "__main__":
    filename = sys.argv[1]
    data = []
    with open(filename) as f:
        for line in f:
            value = int(line.split(":")[0])
            numbers = [int(x) for x in line.split(":")[1].split()]
            data.append([value, numbers])
    print(data)
    output = []
    output = [x[0] for x in data if is_valid(x)]
    print(f"Sum of valid values: {sum(output)}")
