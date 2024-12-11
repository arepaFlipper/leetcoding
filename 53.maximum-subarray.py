from typing import List
# @leet start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res: int = nums[0]

        total: int = 0

        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
            print("n: ", n, "total: ", total, "res: ", res)

        return res
# @leet end
#
# Test Case 1
nums_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
expected_output_1 = 6

print("Test Case 1:")
output_1 = Solution().maxSubArray(nums_1)
print(f"maxSubArray({nums_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
nums_2 = [1]
expected_output_2 = 1

print("\nTest Case 2:")
output_2 = Solution().maxSubArray(nums_2)
print(f"maxSubArray({nums_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
nums_3 = [5, 4, -1, 7, 8]
expected_output_3 = 23

print("\nTest Case 3:")
output_3 = Solution().maxSubArray(nums_3)
print(f"maxSubArray({nums_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

