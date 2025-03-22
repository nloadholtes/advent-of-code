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

def can_construct(target, available, any_matches=False):
    dp = [False] * (len(target) + 1)
    dp[0] = True  # Empty string is always constructible
    
    for i in range(1, len(target) + 1):
        for word in available:
            if (i >= len(word) and 
                target[i-len(word):i] == word and 
                dp[i-len(word)]):
                dp[i] = True
                if any_matches is False:
                    break
    
    return dp[len(target)]

def find_all_constructions(design, patterns):
    dp = [[] for _ in range(len(design) + 1)]
    dp[0] = [[]]  # Empty list of patterns is valid for empty string
    
    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if (i >= len(pattern) and 
                design[i-len(pattern):i] == pattern and 
                dp[i-len(pattern)]):
                # For each valid construction up to i-len(pattern)
                for prev_construction in dp[i-len(pattern)]:
                    # Add this pattern to that construction
                    dp[i].append(prev_construction + [pattern])
    
    return dp[len(design)]  # Returns list of all valid pattern combinations

if __name__ == "__main__":
    data = [x.strip() for x in open(sys.argv[1]).readlines()]
    available = parse_available(data[0])
    designs = []
    for row in data[2:]:
        designs.append(can_construct(row, available))
    print(f"Number of designs we can make: {sum(designs)}")
    designs = []
    for row in data[2:]:
        designs.append(len(find_all_constructions(row, available)))
    print(designs)
    print(f"Using any_matches, number of designs we can make: {sum(designs)}")
