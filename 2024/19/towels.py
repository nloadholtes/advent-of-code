import sys


def parse_available(row):
    return set([x.strip() for x in row.split(",")])

def factor(row, available):
    output = []
    # Look for substrings
    for x in range(len(row)):
        if x in available:
            output.append(x)
            continue
        # Need longest matching substring

    # If there's no martch return false
    return output

def can_construct(target, available):
    dp = [False] * (len(target) + 1)
    dp[0] = True  # Empty string is always constructible
    
    for i in range(1, len(target) + 1):
        for word in available:
            if (i >= len(word) and 
                target[i-len(word):i] == word and 
                dp[i-len(word)]):
                dp[i] = True
                break
    
    return dp[len(target)]

if __name__ == "__main__":
    data = [x.strip() for x in open(sys.argv[1]).readlines()]
    available = parse_available(data[0])
    designs = []
    for row in data[2:]:
        designs.append(can_construct(row, available))
    print(f"Designs: {designs}")
    print(f"Number of designs we can make: {sum(designs)}")
