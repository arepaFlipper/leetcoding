# @leet start
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1

        for idx in range( 1, n+1):
            if offset * 2 == idx:
                offset = idx
            dp[idx] = 1 + dp[idx - offset]
        return dp
# @leet end

# Test Case 1
n_1 = 2
expected_output_1 = [0, 1, 1]

print("Test Case 1:")
output_1 = Solution().countBits(n_1)
print(f"countBits({n_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
n_2 = 5
expected_output_2 = [0, 1, 1, 2, 1, 2]

print("\nTest Case 2:")
output_2 = Solution().countBits(n_2)
print(f"countBits({n_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
n_3 = 0
expected_output_3 = [0]

print("\nTest Case 3:")
output_3 = Solution().countBits(n_3)
print(f"countBits({n_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

