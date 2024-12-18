import sys
from itertools import product

ops = [0,1,2]

def is_valid(row):
    output = False
    value = row[0]
    numbers = row[1]
    total = None
    #breakpoint()
    #print(f"Searching for {value}")
    all_states = list(product(ops, repeat=len(numbers)-1))
    for state in all_states:
        nums = list(numbers)
        nums.reverse()
        total = nums.pop()
        for x in state:
            num = nums.pop()
            if x == 0:
                total = total * num
            if x == 1:
                total = total + num
            # This next check slows it down significantly. Took 12 secs to finish on the m1
            if x == 2:
                total = int(str(total) + str(num))
            #print(total)
            if total > value:
                break
        if total == value:
            #print("FOUND ONE")
            return True
            #print(f"Total for {state}: {total}")

    return output

if __name__ == "__main__":
    filename = sys.argv[1]
    data = []
    with open(filename) as f:
        for line in f:
            value = int(line.split(":")[0])
            numbers = [int(x) for x in line.split(":")[1].split()]
            data.append([value, numbers])
    output = []
    output = [x[0] for x in data if is_valid(x)]
    print(f"Sum of valid values: {sum(output)}")
