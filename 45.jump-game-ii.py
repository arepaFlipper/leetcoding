from typing import List

# @leet start
class Solution:
    def jump(self, nums: List[int]) -> int:
        (left, right) = (0,0)
        res = 0
        while right < (len(nums)-1):
           max_jump = 0
           for idx in range(left, right +1):
               max_jump = max(max_jump, idx + nums[idx])
           left = right + 1
           right = max_jump
           res += 1
        return res
# @leet end

# Test Case 1
nums_1 = [2, 3, 1, 1, 4]
expected_output_1 = 2

print("Test Case 1:")
output_1 = Solution().jump(nums_1)
print(f"jump({nums_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
nums_2 = [2, 3, 0, 1, 4]
expected_output_2 = 2

print("\nTest Case 2:")
output_2 = Solution().jump(nums_2)
print(f"jump({nums_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
nums_3 = [1]
expected_output_3 = 0

print("\nTest Case 3:")
output_3 = Solution().jump(nums_3)
print(f"jump({nums_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

