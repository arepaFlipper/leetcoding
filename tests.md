I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

                https://leetcode.com/problems/happy-number/
                                      
                             202. Happy Number
                  Easy  │ 10049  1387  │ 55.9% of 2.5M



Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

	* Starting with any positive integer, replace the number by the sum of the squares of its digits.
	
	* Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
	
	* Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.



󰛨 Example 1:

	│ Input: n = 19
	│ Output: true
	│ Explanation:
	│ 1^2 + 9^2 = 82
	│ 8^2 + 2^2 = 68
	│ 6^2 + 8^2 = 100
	│ 1^2 + 0^2 + 0^2 = 1

󰛨 Example 2:

	│ Input: n = 2
	│ Output: false



 Constraints:

	* 1 <= n <= 2^31 - 1









The following is my solution to test:

```
# @leet start
class Solution:
    def isHappy(self, n: int) -> bool:
        (slow, fast) = (n,self.sumSquareDigits(n))

        while slow != fast:
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)

        return True if fast == 1 else False

    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n%10) ** 2
            n = n // 10
# @leet end
```
