# @leet start
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for idx in range(len(s)):
            res += self.countPali(s, idx, idx)
            print("❄️  res: ", res)
            res += self.countPali(s, idx, idx + 1)
            print("🐾 res: ", res)
        
        return res
    
    def countPali(self, s, left, right):
        res = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1
            print("res:", res, ", ⬅️  left: ", left, ", ➡️  right: ", right, "\n")
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
