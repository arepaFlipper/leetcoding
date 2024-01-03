I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

https://leetcode.com/problems/palindromic-substrings/
                        
           647. Palindromic Substrings
Medium | 9873  209  | 68.2% of 962.3K | 󰛨 Hints



Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



󰛨 Example 1:

	▎	Input: s = "abc"
	▎	Output: 3
	▎	Explanation: Three palindromic strings: "a", "b", "c".

󰛨 Example 2:

	▎	Input: s = "aaa"
	▎	Output: 6
	▎	Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".



 Constraints:

	* 1 <= s.length <= 1000
	
	* s consists of lowercase English letters.









The following is my solution to test:
```

# @leet start
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for idx in range(len(s)):
            res += self.countPali(s, idx, idx)
            res += self.countPali(s, idx, idx + 1)
        
        return res
    def countPali(self, s, left, right):
        res = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1
        return res
# @leet end
        
```
