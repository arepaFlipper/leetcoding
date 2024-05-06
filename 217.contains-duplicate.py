from typing import List 
# @leet start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = {}

        for num in nums:
            if num in hash_set:
                return True
            else:
                hash_set[num] = 1
        return False

        
# @leet end

# Test Case 1
test_input_1_nums = [1, 2, 3, 1]
expected_output_1 = True
actual_output_1 = Solution().containsDuplicate(test_input_1_nums)
print("Test Case 1:")
print(f"Input: nums = {test_input_1_nums}")
print(f"Output: {actual_output_1}")
print(f"Expected: {expected_output_1}")
if actual_output_1 == expected_output_1:
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")

# Test Case 2
test_input_2_nums = [1, 2, 3, 4]
expected_output_2 = False
actual_output_2 = Solution().containsDuplicate(test_input_2_nums)
print("\nTest Case 2:")
print(f"Input: nums = {test_input_2_nums}")
print(f"Output: {actual_output_2}")
print(f"Expected: {expected_output_2}")
if actual_output_2 == expected_output_2:
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")

# Test Case 3
test_input_3_nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
expected_output_3 = True
actual_output_3 = Solution().containsDuplicate(test_input_3_nums)
print("\nTest Case 3:")
print(f"Input: nums = {test_input_3_nums}")
print(f"Output: {actual_output_3}")
print(f"Expected: {expected_output_3}")
if actual_output_3 == expected_output_3:
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")


