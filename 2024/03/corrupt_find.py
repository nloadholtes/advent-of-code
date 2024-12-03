# Parse looking for mul(X,Y)
# Make sure X and Y are actually numbers
# Multiply
# Add up the muiltiplications.
#
import sys
import re


REGEX_PATTERN = r"mul\((\d+),(\d+)\)"
REGEX_PATTERN2 = r"(mul\((\d+),(\d+)\))|(don't\(\))|(do\(\))"

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
    print("************ part 2 *************")
    muls = re.findall(REGEX_PATTERN2, data)
    skip = False # True  # Pays to read the instructions. It starts assuming muls are enabled.
    counter = 0
    output = []
    for x in muls:
        if "do()" in x[4]:
            skip = False
        if "don't()" in x[3]:
            skip = True
        if skip:
            continue
        if x[1] and x[2]:
            output.append(int(x[1]) * int(x[2]))
        counter += 1
        # breakpoint()
        # if counter > 40:
        #    break
    print(f"Sum of multiplications is: {sum(output)}")
