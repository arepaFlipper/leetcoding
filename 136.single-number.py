# @leet start
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
        
# @leet end
# Test Case 1
nums_1 = [2, 2, 1]
expected_output_1 = 1

print("Test Case 1:")
output_1 = Solution().singleNumber(nums_1)
print(f"singleNumber({nums_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
nums_2 = [4, 1, 2, 1, 2]
expected_output_2 = 4

print("\nTest Case 2:")
output_2 = Solution().singleNumber(nums_2)
print(f"singleNumber({nums_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
nums_3 = [1]
expected_output_3 = 1

print("\nTest Case 3:")
output_3 = Solution().singleNumber(nums_3)
print(f"singleNumber({nums_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

