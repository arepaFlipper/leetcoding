I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

    https://leetcode.com/problems/target-sum/
                        
                 494. Target Sum
     Medium | 10508  347  | 46.4% of 1.2M



You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

	* For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.



󰛨 Example 1:

	▎	Input: nums = [1,1,1,1,1], target = 3
	▎	Output: 5
	▎	Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
	▎	-1 + 1 + 1 + 1 + 1 = 3
	▎	+1 - 1 + 1 + 1 + 1 = 3
	▎	+1 + 1 - 1 + 1 + 1 = 3
	▎	+1 + 1 + 1 - 1 + 1 = 3
	▎	+1 + 1 + 1 + 1 - 1 = 3

󰛨 Example 2:

	▎	Input: nums = [1], target = 1
	▎	Output: 1



 Constraints:

	* 1 <= nums.length <= 20
	
	* 0 <= nums[i] <= 1000
	
	* 0 <= sum(nums[i]) <= 1000
	
	* -1000 <= target <= 1000









The following is my solution to test:
```
# @leet start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp: Dict = {}

        def backtrack(idx, total):
            if idx == len(nums):
                return 1 if (total == target) else 0
            
            if (idx, total) in dp:
                return dp[(idx, total)]

            dp[(idx,total)] = backtrack(idx+1, total + nums[idx]) + backtrack(idx+1, total - nums[idx])
            return dp[(idx,total)]
        return backtrack(0,0)
# @leet end
```
