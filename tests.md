I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

https://leetcode.com/problems/distinct-subsequences/
                        
           115. Distinct Subsequences
      Hard | 6397  280  | 46.1% of 788.6K



Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.



󰛨 Example 1:

	▎	Input: s = "rabbbit", t = "rabbit"
	▎	Output: 3
	▎	Explanation:
	▎	As shown below, there are 3 ways you can generate "rabbit" from s.
	▎	rabbbit
	▎	rabbbit
	▎	rabbbit

󰛨 Example 2:

	▎	Input: s = "babgbag", t = "bag"
	▎	Output: 5
	▎	Explanation:
	▎	As shown below, there are 5 ways you can generate "bag" from s.
	▎	babgbag
	▎	babgbag
	▎	babgbag
	▎	babgbag
	▎	babgbag



 Constraints:

	* 1 <= s.length, t.length <= 1000
	
	* s and t consist of English letters.



The following is my solution to test:
```
# @leet start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        for idx in range(len(s) +1):
            cache[(idx,len(t))] = 1
        for jdx in range(len(t)):
            cache[(len(s), jdx)] = 0

        for i in range(len(s) -1, -1,-1):
            for j in range(len(t) -1, -1, -1):
                if s[i] == t[j]:
                    cache[(i,j)] = cache[(i+1,j+1)] + cache[(i+1,j)]
                else:
                    cache[(i,j)] = cache[(i+1,j)]
        return cache[(0,0)]
# @leet end
```
