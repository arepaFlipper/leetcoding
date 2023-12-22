# @leet start
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(idx, current_string):
            if len(current_string) == len(digits):
                res.append(current_string)
                return
            for char in digit_to_char[digits[idx]]:
                backtrack(idx + 1, current_string + char)

        if digits:
            backtrack(0, "")

        return res


solution = Solution()

# Test Case 1
input_digits_1 = "23"
expected_output_1 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
result_1 = solution.letterCombinations(input_digits_1)

print("Test Case 1:")
print("Input:")
print("Digits:", input_digits_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_digits_2 = ""
expected_output_2 = []
result_2 = solution.letterCombinations(input_digits_2)

print("\nTest Case 2:")
print("Input:")
print("Digits:", input_digits_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
input_digits_3 = "2"
expected_output_3 = ["a", "b", "c"]
result_3 = solution.letterCombinations(input_digits_3)

print("\nTest Case 3:")
print("Input:")
print("Digits:", input_digits_3)
print("Output:", result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
        
# @leet end
