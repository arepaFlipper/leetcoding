# @leet start
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hash = {}
        for word in wordDict:
            for idx in range(len(s)):
                sub_string = s[idx:len(word)]
                print("""🔕   \x1b[1;34;40m139.word-break-python3.py:9  sub_string:""") ## DELETEME:
                print(sub_string) ## DELETEME:
                print('\x1b[0m') ## DELETEME:
                if len(sub_string) < len(word):
                    break
                if sub_string == word:
                    return True
        return False
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
