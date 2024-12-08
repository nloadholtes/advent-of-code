import sys


if __name__ == "__main__":
    filename = sys.argv[1]
    data = []
    with open(filename) as f:
        for line in f:
            value = int(line.split(":")[0])
            numbers = [int(x) for x in line.split(":")[1].split()]
            data.append([value, numbers])
    print(data)
