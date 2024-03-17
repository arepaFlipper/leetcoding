from typing import List

# @leet start
class Solution:
    def rob(self, nums: List[int]) -> int:
        (rob1, rob2) = (0,0)

        print("👉 nums:", nums)
        for house in nums:
            tmp = max(house + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
            print("house:", house,", tmp:", tmp, ", rob1:", rob1, ", rob2:", rob2)
            # __import__('pdb').set_trace() ##DELETEME:
        return tmp
         
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

