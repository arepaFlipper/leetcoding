from typing import List
# @leet start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        (current_max, current_min) = (1,1)

        for num in nums:
            cur_prod = num * current_max
            current_max = max(cur_prod, num * current_min, num)
            current_min = min(cur_prod, num * current_min, num)
            res = max(res, current_max)
        return res


solution = Solution()

# Test Case 1
nums_1 = [2, 3, -2, 4]
expected_output_1 = 6
result_1 = solution.maxProduct(nums_1)

print("Test Case 1:")
print("Input:")
print("nums:", nums_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
nums_2 = [-2, 0, -1]
expected_output_2 = 0
result_2 = solution.maxProduct(nums_2)

print("\nTest Case 2:")
print("Input:")
print("nums:", nums_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
nums_3 = [-4,-3]
expected_output_3 = 12
result_3 = solution.maxProduct(nums_3)

print("\nTest Case 3:")
print("Input:")
print("nums:", nums_3)
print("Output:", result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output\nExpected:", expected_output_3)

