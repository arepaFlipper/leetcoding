# @leet start
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for idx in range(len(nums)):
            res += idx - nums[idx]
        return res
# @leet end

# Test Case 1
nums_1 = [3, 0, 1]
expected_output_1 = 2

print("Test Case 1:")
output_1 = Solution().missingNumber(nums_1)
print(f"missingNumber({nums_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
nums_2 = [0, 1]
expected_output_2 = 2

print("\nTest Case 2:")
output_2 = Solution().missingNumber(nums_2)
print(f"missingNumber({nums_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
nums_3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
expected_output_3 = 8

print("\nTest Case 3:")
output_3 = Solution().missingNumber(nums_3)
print(f"missingNumber({nums_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

