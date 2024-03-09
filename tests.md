I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

              https://leetcode.com/problems/multiply-strings/
                                      
                            43. Multiply Strings
                  Medium  │ 6898  3259  │ 40.1% of 1.9M



Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



󰛨 Example 1:

	│ Input: num1 = "2", num2 = "3"
	│ Output: "6"

󰛨 Example 2:

	│ Input: num1 = "123", num2 = "456"
	│ Output: "56088"



 Constraints:

	* 1 <= num1.length, num2.length <= 200
	
	* num1 and num2 consist of digits only.
	
	* Both num1 and num2 do not contain any leading zero, except the number 0 itself.








The following is my solution to test:

```
# @leet start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
    
        res = [0] * (len(num1)+len(num2))
        (num1, num2) = (num1[::-1], num2[::-1])
        for idx in range(len(num1)):
            for jdx in range(len(num2)):
                digit = int(num1[idx])* int(num2[jdx])
                res[idx + jdx] += digit
                res[idx + jdx + 1] += res[idx + jdx]//10
                res[idx + jdx] = res[idx+jdx] % 10

        (res, beg) = (res[::-1], 0)
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str,res[beg:])
        return "".join(res)
                
# @leet end
```
