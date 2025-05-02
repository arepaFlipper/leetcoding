# @leet start
class Solution:
    def hammingWeight(self, n: int) -> int:
        res: int = 0
        while n:
            res += n % 2
            n = n >> 1
        return res
# @leet end

# Define test cases as (binary_string, expected_output)
test_cases = [
    ('00000000000000000000000000001011', 3),
    ('00000000000000000000000010000000', 1),
    ('11111111111111111111111111111101', 31),
    ('00000000000000000000000000000000', 0),
    ('11111111111111111111111111111111', 32),
]

# Run test suite
for idx, (binary_str, expected) in enumerate(test_cases, 1):
    n = int(binary_str, 2)
    output = Solution().hammingWeight(n)
    print(f"Test Case {idx}: hammingWeight({binary_str}) => Output: {output}")
    if output == expected:
        print("✅ Expected Output")
    else:
        print(f"❌ Unexpected Output (Expected: {expected})")
