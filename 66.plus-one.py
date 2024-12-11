# @leet start
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        one = 1
        idx = 0
        digits = digits[::-1]

        while one:
            if idx < len(digits):
                if digits[idx] == 9:
                    digits[idx] = 0
                else:
                    digits[idx] += 1
                    one = 0

            else:
                digits.append(one)
                one = 0
            idx += 1
        return digits[::-1]
        
# @leet end

# Test Case 1
test_input_1_digits = [1, 2, 3]
expected_output_1 = [1, 2, 4]
output_1 = Solution().plusOne(test_input_1_digits)
print("Test Case 1:")
print(f"Input: digits = {test_input_1_digits}")
print(f"Output: {output_1}")
print(f"Expected: {expected_output_1}")
if output_1 == expected_output_1:
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")

# Test Case 2
test_input_2_digits = [4, 3, 2, 1]
expected_output_2 = [4, 3, 2, 2]
output_2 = Solution().plusOne(test_input_2_digits)
print("\nTest Case 2:")
print(f"Input: digits = {test_input_2_digits}")
print(f"Output: {output_2}")
print(f"Expected: {expected_output_2}")
if output_2 == expected_output_2:
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")

# Test Case 3
test_input_3_digits = [9]
expected_output_3 = [1, 0]
output_3 = Solution().plusOne(test_input_3_digits)
print("\nTest Case 3:")
print(f"Input: digits = {test_input_3_digits}")
print(f"Output: {output_3}")
print(f"Expected: {expected_output_3}")
if output_3 == expected_output_3:
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")

