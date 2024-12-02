# 

import sys

def get_data(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append([int(x) for x in line.split()])
    return data

def is_safe(row):
    prev = None
    prev_diff = None
    #print(row)
    for x in row:
        if not prev:
            prev= x
            continue
        diff = x - prev
        #print(f"{x} - {prev} = {diff}")
        prev = x
        if not prev_diff:
            prev_diff = diff
        if diff * prev_diff < 0:
            #print("unsafe (diff trend)")
            return False
        diff = abs(diff)
        if diff == 0 or diff > 3:
            #print("unsafe")
            return False
    return True

def main():
    data = []
    filename = sys.argv[1]
    data = get_data(filename)
    output = [1 for row in data if is_safe(row)]
    print(f"Safe reports: {sum(output)}")



if __name__ == "__main__":
    main()
