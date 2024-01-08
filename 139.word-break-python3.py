# @leet start
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for idx in range(len(s) -1, -1,-1):
            for word in wordDict:
                if (idx + len(word)) <= len(s) and (s[idx: idx+len(word)] == word):
                    dp[idx] = dp[idx+len(word)]
                if dp[idx]:
                    break

        return dp[0]

# @leet end

solution = Solution()

# Test Case 1
s1, wordDict1 = "leetcode", ["leet", "code"]
expected_output_1 = True

print("Test Case 1:")
output_1 = solution.wordBreak(s1, wordDict1)
print("wordBreak(\"leetcode\", [\"leet\",\"code\"]) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
s2, wordDict2 = "applepenapple", ["apple", "pen"]
expected_output_2 = True

print("\nTest Case 2:")
output_2 = solution.wordBreak(s2, wordDict2)
print("wordBreak(\"applepenapple\", [\"apple\",\"pen\"]) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
s3, wordDict3 = "catsandog", ["cats", "dog", "sand", "and", "cat"]
expected_output_3 = False

print("\nTest Case 3:")
output_3 = solution.wordBreak(s3, wordDict3)
print("wordBreak(\"catsandog\", [\"cats\",\"dog\",\"sand\",\"and\",\"cat\"]) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
# @leet end
