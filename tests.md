I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

        https://leetcode.com/problems/longest-palindromic-substring/
                                      
                      5. Longest Palindromic Substring
            Medium  │ 29385  1793  │ 34.2% of 9.4M │ 󰛨 Hints



Given a string s, return the longest palindromic substring in s.



󰛨 Example 1:

	│ Input: s = "babad"
	│ Output: "bab"
	│ Explanation: "aba" is also a valid answer.

󰛨 Example 2:

	│ Input: s = "cbbd"
	│ Output: "bb"



 Constraints:

	* 1 <= s.length <= 1000
	
	* s consist of only digits and English letters.






The following is my solution to test:

```py
# @leet start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        for idx in range(len(s)):
            (left, right) = (idx, idx)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1 ) > res_len:
                    res = s[left: right + 1]
                    res_len = right - left + 1
                left -= 1
                right += 1

            (left, right) = (idx, idx + 1)
            while left >=0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    res = s[left : right +1 ]
                    res_len = right - left + 1
                left -= 1
                right += 1

        return res
# @leet end
```
