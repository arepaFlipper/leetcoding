I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

                https://leetcode.com/problems/jump-game-ii/
                                      
                              45. Jump Game II
                   Medium | 14042  522  | 40.3% of 2.8M



You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

	* 0 <= j <= nums[i] and
	
	* i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



󰛨 Example 1:

	▎ Input: nums = [2,3,1,1,4]
	▎ Output: 2
	▎ Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

󰛨 Example 2:

	▎ Input: nums = [2,3,0,1,4]
	▎ Output: 2



 Constraints:

	* 1 <= nums.length <= 10^4
	
	* 0 <= nums[i] <= 1000
	
	* It's guaranteed that you can reach nums[n - 1].


The following is my solution to test:

```
# @leet start
class Solution:
    def jump(self, nums: List[int]) -> int:
        (left, right) = (0,0)
        res = 0
        while right < (len(nums)-1):
           max_jump = 0
           for idx in range(left, right +1):
               max_jump = max(max_jump, idx + nums[idx])
           left = right + 1
           right = max_jump
           res += 1
        return res
# @leet end
```
