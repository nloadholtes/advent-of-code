
import sys


PHRASE = "XMAS"


if __name__ == "__main__":
    filename = sys.argv[1]
    data = []

    with open(filename) as f:
        for line in f:
            data.append(line)

    

