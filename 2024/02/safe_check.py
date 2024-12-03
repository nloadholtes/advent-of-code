# 

import sys

def get_data(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append([int(x) for x in line.split()])
    return data

def is_safe(row, tolerance=0):
    prev = None
    prev_diff = None
    safe_tracker = []
    tolerance_count = 0
    # print(row)
    for x in row:
        if not prev:
            prev= x
            continue
        diff = x - prev
        # print(f"{x} - {prev} = {diff}")
        if not prev_diff:
            prev_diff = diff
        if diff * prev_diff < 0:
            # print("unsafe (diff trend)")
            if tolerance_count < tolerance:
                tolerance_count += 1
                continue
            safe_tracker.append(False)
            prev = x
            continue
        diff = abs(diff)
        if diff == 0 or diff > 3:
            #print("unsafe" )
            if tolerance_count < tolerance:
                tolerance_count += 1
                continue
            safe_tracker.append(False)
            prev = x
            continue
        prev = x
        safe_tracker.append(True)
    output = True if safe_tracker.count(False) == 0 else False
    return output  # , safe_tracker

def main():
    data = []
    filename = sys.argv[1]
    data = get_data(filename)
    output = [1 for row in data if is_safe(row)]
    print(f"Safe: {sum(output)}")
    
    within_tolerance = [1 for row in data if is_safe(row, tolerance=1)]
    print(f"Safe within tolerance of 1: {sum(within_tolerance)}")



if __name__ == "__main__":
    main()
