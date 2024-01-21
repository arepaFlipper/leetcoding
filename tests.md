I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

                  https://leetcode.com/problems/regular-expression-matching/
                                               
                                10. Regular Expression Matching
                             Hard | 11783  2046  | 28.0% of 3.2M



Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

	* '.' Matches any single character.
	
	* '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).



󰛨 Example 1:

	▎	Input: s = "aa", p = "a"
	▎	Output: false
	▎	Explanation: "a" does not match the entire string "aa".

󰛨 Example 2:

	▎	Input: s = "aa", p = "a*"
	▎	Output: true
	▎	Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

󰛨 Example 3:

	▎	Input: s = "ab", p = ".*"
	▎	Output: true
	▎	Explanation: ".*" means "zero or more (*) of any character (.)".



 Constraints:

	* 1 <= s.length <= 20
	
	* 1 <= p.length <= 20
	
	* s contains only lowercase English letters.
	
	* p contains only lowercase English letters, '.', and '*'.
	
	* It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.



The following is my solution to test:
```
# @leet start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = [[False] * (len(p) + 1) for i in range(len(s)+1)]
        cache[len(s)][len(p)] = True

        for idx in range(len(s), -1,-1):
            for jdx in range(len(p)-1,-1,-1):
                match = idx < len(s) and (s[idx] == p[jdx] or p[jdx] == ".")

                if (jdx +1) < len(p) and p[jdx +1] == "*":
                    cache[idx][jdx] = cache[idx][jdx+2]
                    if match:
                        cache[idx][jdx] = cache[idx+1][jdx] or cache[idx][jdx]
                elif match:
                    cache[idx][jdx] = cache[idx+1][jdx +1]
        return cache[0][0]
        
# @leet end
```
