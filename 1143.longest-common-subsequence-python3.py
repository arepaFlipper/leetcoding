# @leet start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [[0 for jdx in range(len(text2) + 1)] for idx in range(len(text1) + 1)]

        for idx in range(len(text1) - 1, -1, -1):
            for jdx in range(len(text2) - 1, -1, -1):
                if text1[idx] == text2[jdx]:
                    matrix[idx][jdx] = 1 + matrix[idx + 1][jdx + 1]
                else:
                    matrix[idx][jdx] = max(matrix[idx][jdx + 1], matrix[idx + 1][jdx])

        return matrix[0][0]

# @leet end

solution = Solution()

# Test Case 1
text1_1, text2_1 = "abcde", "ace"
expected_output_1 = 3

print("Test Case 1:")
output_1 = solution.longestCommonSubsequence(text1_1, text2_1)
print(f'longestCommonSubsequence("{text1_1}", "{text2_1}") => Output:', output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
text1_2, text2_2 = "abc", "abc"
expected_output_2 = 3

print("\nTest Case 2:")
output_2 = solution.longestCommonSubsequence(text1_2, text2_2)
print(f'longestCommonSubsequence("{text1_2}", "{text2_2}") => Output:', output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
text1_3, text2_3 = "abc", "def"
expected_output_3 = 0

print("\nTest Case 3:")
output_3 = solution.longestCommonSubsequence(text1_3, text2_3)
print(f'longestCommonSubsequence("{text1_3}", "{text2_3}") => Output:', output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
