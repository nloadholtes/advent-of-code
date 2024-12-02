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
    safe_tracker = []
    # print(row)
    for x in row:
        if not prev:
            prev= x
            continue
        diff = x - prev
        # print(f"{x} - {prev} = {diff}")
        prev = x
        if not prev_diff:
            prev_diff = diff
        if diff * prev_diff < 0:
            #print("unsafe (diff trend)")
            safe_tracker.append(False)
            continue
        diff = abs(diff)
        if diff == 0 or diff > 3:
            # print("unsafe")
            safe_tracker.append(False)
            continue
        safe_tracker.append(True)
    output = True if safe_tracker.count(False) == 0 else False
    return output, safe_tracker

def main():
    data = []
    filename = sys.argv[1]
    data = get_data(filename)
    output = []
    safe_tracker=[]
    for row in data:
        s, s_t = is_safe(row)
        output.append(1 if s else 0)
        safe_tracker.append(s_t)
    print(f"Safe reports: {sum(output)}")
    print(safe_tracker)
    print(f"Potentially safe: {sum([1 for x in safe_tracker if x.count(False)<2])}")



if __name__ == "__main__":
    main()
