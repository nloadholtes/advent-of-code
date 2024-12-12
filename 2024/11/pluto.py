import sys
from functools import lru_cache

def analyze_growth(data, target_iterations=25):
    """Claude came up with this as an idea to explore the growth rate to see if there
        was a creative way to just calculate the value directly. The growth rate was around
        1.51, but that was variable between iterations and directly computing it for the 
        75th round resulted in numbers that were too high"""
    counts = []
    current_data = data.copy()
    
    for i in range(target_iterations):
        tmp_data = []
        for num in current_data:
            if not num:
                continue
            if len(num) % 2 == 0:
                size = int(len(num)/2)
                tmp_data.append(num[0:size])
                tmp_data.append(str(int(num[size:])))
            elif int(num) == 0:
                tmp_data.append("1")
            else:
                tmp_data.append(str(2024*int(num)))
                
        current_data = tmp_data
        counts.append(len(current_data))
        
        # Calculate growth rate
        if i > 0:
            growth_rate = counts[i] / counts[i-1]
            print(f"Iteration {i+1}: Count = {counts[i]}, Growth Rate = {growth_rate:.2f}")

    return counts

@lru_cache(maxsize=None)
def calc_number(num):
    tmp_data = []
    if len(num) %2==0:
        #breakpoint()
        size = int(len(num)/2)
        tmp_data.append(num[0:size])
        tmp_data.append(str(int(num[size:])))
    elif int(num) == 0:
        tmp_data.append("1")
    else:
        tmp_data.append(str(2024*int(num)))
    return tuple(tmp_data)

if __name__ == "__main__":
    data = open(sys.argv[1]).read().strip().split()
    blinks = int(sys.argv[2])
    for x in range(blinks):
        tmp_data = []
        for num in data:
            if not num:
                continue
            for y in calc_number(num):
                tmp_data.append(y)

        #print(f"--len: {len(tmp_data)}")
        #print(" ".join(tmp_data))
        data = tmp_data

    print(f"Length of stones: {len(data)}")
    print("2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2")
    #print(analyze_growth(data, target_iterations=blinks))
    #print(" ".join(data))


