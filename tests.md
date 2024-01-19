I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

                https://leetcode.com/problems/edit-distance/
                                      
                             72. Edit Distance
                   Medium | 14298  192  | 55.9% of 1.4M



Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

	* Insert a character
	
	* Delete a character
	
	* Replace a character



󰛨 Example 1:

	▎	Input: word1 = "horse", word2 = "ros"
	▎	Output: 3
	▎	Explanation: 
	▎	horse -> rorse (replace 'h' with 'r')
	▎	rorse -> rose (remove 'r')
	▎	rose -> ros (remove 'e')

󰛨 Example 2:

	▎	Input: word1 = "intention", word2 = "execution"
	▎	Output: 5
	▎	Explanation: 
	▎	intention -> inention (remove 't')
	▎	inention -> enention (replace 'i' with 'e')
	▎	enention -> exention (replace 'n' with 'x')
	▎	exention -> exection (replace 'n' with 'c')
	▎	exection -> execution (insert 'u')



 Constraints:

	* 0 <= word1.length, word2.length <= 500
	
	* word1 and word2 consist of lowercase English letters.



The following is my solution to test:
```
# @leet start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp: List = [[float("inf")] * (len(word2) +1) for idx in range(len(word1) +1)]

        for idx in range (len(word2)+1):
            dp[len(word1)][idx] = len(word2) - idx

        for idx in range(len(word1) +1):
            dp[idx][len(word2)] = len(word1) - idx

        for idx in range(len(word1)-1,-1,-1):
            for jdx in range(len(word2)-1,-1,-1):
                if word1[idx] == word2[jdx]:
                    dp[idx][jdx] = dp[idx+1][jdx+1]
                else:
                    dp[idx][jdx] = 1 + min(dp[idx + 1][jdx], dp[idx][jdx+1], dp[idx+1][jdx+1])
        return dp[0][0]
        
# @leet end
```
