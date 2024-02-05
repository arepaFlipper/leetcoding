I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

              https://leetcode.com/problems/maximum-subarray/
                                      
                            53. Maximum Subarray
                  Medium | 33100  1390  | 50.6% of 7.2M



Given an integer array nums, find the subarray with the largest sum, and return its sum.



󰛨 Example 1:

	▎ Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
	▎ Output: 6
	▎ Explanation: The subarray [4,-1,2,1] has the largest sum 6.

󰛨 Example 2:

	▎ Input: nums = [1]
	▎ Output: 1
	▎ Explanation: The subarray [1] has the largest sum 1.

󰛨 Example 3:

	▎ Input: nums = [5,4,-1,7,8]
	▎ Output: 23
	▎ Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.



 Constraints:

	* 1 <= nums.length <= 10^5
	
	* -10^4 <= nums[i] <= 10^4



Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.






The following is my solution to test:

```
# @leet start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res: int = nums[0]

        total: int = 0

        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0

        return res
# @leet end
```
