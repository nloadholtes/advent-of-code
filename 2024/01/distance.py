# Day 1
#
# Pair up the smallest number in the left with the smallest on the right
# Sub to get the difference 
# Add up the difference
import sys

def read_and_split(filename):
    """Open the given file, return 2 lists for the data in the file."""
    left, right = [], []
    with open(filename) as f:
        for line in f:
            l, r = line.split()
            left.append(l)
            right.append(r)
    return sorted(left), sorted(right)

def main():
    filename = sys.argv[1]
    left, right = read_and_split(filename)
    # Get the differences
    differences = []
    for x in zip(left, right):
        differences.append(abs(int(x[0])-int(x[1])))
    print(f"differences: {sum(differences)}")


if __name__ == "__main__":
    main()
