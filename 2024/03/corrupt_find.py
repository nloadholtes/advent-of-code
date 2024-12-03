# Parse looking for mul(X,Y)
# Make sure X and Y are actually numbers
# Multiply
# Add up the muiltiplications.
#
import sys
import re


REGEX_PATTERN = r"mul\((\d+),(\d+)\)"

if __name__ == "__main__":
    filename = sys.argv[1]
    muls = []
    f = open(filename)
    data = f.read()
    f.close()
    muls = re.findall(REGEX_PATTERN, data)
    print(f"Saw {len(muls)} muls")
    output = []
    for x in muls:
        output.append(int(x[0]) * int(x[1]))
    print(f"Sum of muiltiplications is: {sum(output)}")
