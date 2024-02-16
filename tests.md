I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

                https://leetcode.com/problems/counting-bits/
                                      
                             338. Counting Bits
               Easy | 10835  508  | 78.0% of 1.3M | 󰛨 Hints



Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.



󰛨 Example 1:

	▎ Input: n = 2
	▎ Output: [0,1,1]
	▎ Explanation:
	▎ 0 --> 0
	▎ 1 --> 1
	▎ 2 --> 10

󰛨 Example 2:

	▎ Input: n = 5
	▎ Output: [0,1,1,2,1,2]
	▎ Explanation:
	▎ 0 --> 0
	▎ 1 --> 1
	▎ 2 --> 10
	▎ 3 --> 11
	▎ 4 --> 100
	▎ 5 --> 101



 Constraints:

	* 0 <= n <= 10^5



Follow up:

	* It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
	
	* Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?



Follow up: If this function is called many times, how would you optimize it?






The following is my solution to test:

```
# @leet start
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1

        for idx in range( 1, n+1):
            if offset * 2 == idx:
                offset = idx
            dp[idx] = 1 + dp[idx - offset]
        return dp
# @leet end
```
