# @leet start
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for left in range(len(s)):
            right = left
            while (0<= left) and (right<len(s)):
                if s[left] == s[right]:
                    res = res + 1
                left = left - 1
                right = right + 1

        for left in range(len(s)):
            right = left +1
            while (0<= left) and (right<len(s)):
                if s[left] == s[right]:
                    res = res + 1
                left = left - 1
                right = right + 1
        return res

solution = Solution()

# Test Case 1
input_str_1 = "abc"
expected_output_1 = 3
result_1 = solution.countSubstrings(input_str_1)

print("Test Case 1:")
print("Input:")
print("s:", input_str_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_str_2 = "aaa"
expected_output_2 = 6
result_2 = solution.countSubstrings(input_str_2)

print("\nTest Case 2:")
print("Input:")
print("s:", input_str_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Additional Test Case
input_str_3 = "racecar"
expected_output_3 = 10
result_3 = solution.countSubstrings(input_str_3)

print("\nAdditional Test Case:")
print("Input:")
print("s:", input_str_3)
print("Output:", result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output, \n Expected: ", expected_output_3)
# @leet end
