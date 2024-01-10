I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

https://leetcode.com/problems/partition-equal-subset-sum/
                        
         416. Partition Equal Subset Sum
     Medium | 11836  222  | 46.2% of 1.6M



Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.



󰛨 Example 1:

	▎	Input: nums = [1,5,11,5]
	▎	Output: true
	▎	Explanation: The array can be partitioned as [1, 5, 5] and [11].

󰛨 Example 2:

	▎	Input: nums = [1,2,3,5]
	▎	Output: false
	▎	Explanation: The array cannot be partitioned into equal sum subsets.



 Constraints:

	* 1 <= nums.length <= 200
	
	* 1 <= nums[i] <= 100








The following is my solution to test:
```
# @leet start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for idx in range(len(nums) -1, -1, -1):
            next_dp = set()
            for t in dp:
                if (t + nums[idx]) == target:
                    return True
                next_dp.add(t + nums[idx])
                next_dp.add(t)
            dp = next_dp
        return False
# @leet end
```
