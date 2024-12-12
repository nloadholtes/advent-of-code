from functools import lru_cache
import sys

@lru_cache(maxsize=None)
def calc_numbers_count(num, iterations):
    if iterations == 0:
        return 1
    
    # Calculate the next numbers
    if len(num) % 2 == 0:
        size = int(len(num)/2)
        return (calc_numbers_count(num[0:size], iterations-1) + 
                calc_numbers_count(str(int(num[size:])), iterations-1))
    elif int(num) == 0:
        return calc_numbers_count("1", iterations-1)
    else:
        return calc_numbers_count(str(2024*int(num)), iterations-1)

def total_numbers(data, iterations):
    return sum(calc_numbers_count(num, iterations) for num in data)


if __name__ == "__main__":
    data = open(sys.argv[1]).read().strip().split()
    blinks = int(sys.argv[2])
    print(f"Sum for {blinks} blinks is {total_numbers(data, blinks)}")

