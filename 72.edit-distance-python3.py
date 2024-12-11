# @leet start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp: List = [[float("inf")] * (len(word2) + 1) for idx in range(len(word1) + 1)]

        for idx in range(len(word2) + 1):
            dp[len(word1)][idx] = len(word2) - idx

        for idx in range(len(word1) + 1):
            dp[idx][len(word2)] = len(word1) - idx

        for idx in range(len(word1) - 1, -1, -1):
            for jdx in range(len(word2) - 1, -1, -1):
                if word1[idx] == word2[jdx]:
                    dp[idx][jdx] = dp[idx + 1][jdx + 1]
                else:
                    dp[idx][jdx] = 1 + min(dp[idx + 1][jdx], dp[idx][jdx + 1], dp[idx + 1][jdx + 1])
        return dp[0][0]
# @leet end

solution = Solution()

# Test Case 1
word1_1, word2_1 = "horse", "ros"
expected_output_1 = 3

print("Test Case 1:")
output_1 = solution.minDistance(word1_1, word2_1)
print(f'minDistance("{word1_1}", "{word2_1}") => Output:', output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
word1_2, word2_2 = "intention", "execution"
expected_output_2 = 5

print("\nTest Case 2:")
output_2 = solution.minDistance(word1_2, word2_2)
print(f'minDistance("{word1_2}", "{word2_2}") => Output:', output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

