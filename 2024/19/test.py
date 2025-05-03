def can_construct(design, patterns):
    dp = [False] * (len(design) + 1)
    dp[0] = True  # Empty string is always constructible
    
    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if (i >= len(pattern) and 
                design[i-len(pattern):i] == pattern and 
                dp[i-len(pattern)]):
                dp[i] = True
                break
    breakpoint()
    return dp[len(design)]

# Test cases
patterns = {'r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br'}
print(can_construct('brwrr', patterns))  # Should print True
print(can_construct('ubwu', patterns))   # Should print False
print(can_construct("bbrgwb", patterns))
print(can_construct("bwurrg", patterns))
