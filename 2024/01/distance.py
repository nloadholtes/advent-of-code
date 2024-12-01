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
            left.append(int(l))
            right.append(int(r))
    return sorted(left), sorted(right)

def similarity(left, right):
    """Return the count of left multiplied by how many times it appears in the right"""
    similarity = []
    for x in left:
        similarity.append(right.count(x) * x)
    return similarity


def main():
    filename = sys.argv[1]
    left, right = read_and_split(filename)
    # Get the differences
    differences = []
    for x in zip(left, right):
        differences.append(abs(x[0]-x[1]))
    print(f"differences: {sum(differences)}")
    print(f"similarity score: {sum(similarity(left, right))}")

if __name__ == "__main__":
    main()
