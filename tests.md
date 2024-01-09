I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

https://leetcode.com/problems/longest-increasing-subsequence/
                        
       300. Longest Increasing Subsequence
     Medium | 20216  408  | 54.7% of 2.8M



Given an integer array nums, return the length of the longest strictly increasing subsequence.



󰛨 Example 1:

	▎	Input: nums = [10,9,2,5,3,7,101,18]
	▎	Output: 4
	▎	Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

󰛨 Example 2:

	▎	Input: nums = [0,1,0,3,2,3]
	▎	Output: 4

󰛨 Example 3:

	▎	Input: nums = [7,7,7,7,7,7,7]
	▎	Output: 1



 Constraints:

	* 1 <= nums.length <= 2500
	
	* -10^4 <= nums[i] <= 10^4



Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?










The following is my solution to test:
```
# @leet start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for idx in range(len(nums) -1, -1, -1):
            for jdx in range(idx+1, len(nums)):
                if nums[idx] < nums[jdx]:
                    LIS[idx] = max(LIS[idx], 1 + LIS[jdx])
        return max(LIS)
        
# @leet end
```
