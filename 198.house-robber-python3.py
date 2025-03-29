from typing import List

# @leet start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
    
        cache = [0] * len(nums)
        cache[0] = nums[0]
        cache[1] = max(nums[0],nums[1])

        for idx in range(2, len(nums)):
            cache[idx] = max(cache[idx - 1], nums[idx] + cache[idx -2])

        return cache[-1]
         
# @leet end

# Test Case 1
test_input_1_nums = [1, 2, 3, 1]
expected_output_1 = 4
actual_output_1 = Solution().rob(test_input_1_nums)
print("Test Case 1:")
print(f"Input: nums = {test_input_1_nums}")
print(f"Output: {actual_output_1}")
print(f"Expected: {expected_output_1}")
if actual_output_1 == expected_output_1:
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")

# Test Case 2
test_input_2_nums = [2, 7, 9, 3, 1]
expected_output_2 = 12
actual_output_2 = Solution().rob(test_input_2_nums)
print("\nTest Case 2:")
print(f"Input: nums = {test_input_2_nums}")
print(f"Output: {actual_output_2}")
print(f"Expected: {expected_output_2}")
if actual_output_2 == expected_output_2:
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")

