I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

    https://leetcode.com/problems/word-break/
                        
                 139. Word Break
     Medium | 16637  731  | 46.5% of 3.4M



Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



󰛨 Example 1:

	▎	Input: s = "leetcode", wordDict = ["leet","code"]
	▎	Output: true
	▎	Explanation: Return true because "leetcode" can be segmented as "leet code".

󰛨 Example 2:

	▎	Input: s = "applepenapple", wordDict = ["apple","pen"]
	▎	Output: true
	▎	Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
	▎	Note that you are allowed to reuse a dictionary word.

󰛨 Example 3:

	▎	Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
	▎	Output: false



 Constraints:

	* 1 <= s.length <= 300
	
	* 1 <= wordDict.length <= 1000
	
	* 1 <= wordDict[i].length <= 20
	
	* s and wordDict[i] consist of only lowercase English letters.
	
	* All the strings of wordDict are unique.










The following is my solution to test:
```

# @leet start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for idx in range(len(s)-1, -1,-1):
            for w in wordDict:
                if ((idx + len(w)) <= len(s)) and (s[idx:idx+len(w)] == w):
                    dp[idx] = dp[idx+len(w)]
                if dp[idx]:
                    break
        return dp[0]
# @leet end-
        
```
