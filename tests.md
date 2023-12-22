I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

https://leetcode.com/problems/letter-combinations-of-a-phone-number/
                        
    17. Letter Combinations of a Phone Number
     Medium | 17676  926  | 59.3% of 3.1M



Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
img->(https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)



󰛨 Example 1:

	▎	Input: digits = "23"
	▎	Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

󰛨 Example 2:

	▎	Input: digits = ""
	▎	Output: []

󰛨 Example 3:

	▎	Input: digits = "2"
	▎	Output: ["a","b","c"]



 Constraints:

	* 0 <= digits.length <= 4
	* digits[i] is a digit in the range ['2', '9'].







The following is my solution to test:
```
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(idx, current_string):
            if len(current_string) == len(digits):
                res.append(current_string)
                return
            for char in digit_to_char[digits[idx]]:
                backtrack(idx + 1 , current_string + char)

        if digits:
            backtrack(0, "")

        return res
        
```
