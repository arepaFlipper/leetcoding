I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

           https://leetcode.com/problems/subsets-ii/
                               
                        90. Subsets II
             Medium | 9262  266  | 56.7% of 1.5M



Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



󰛨 Example 1:

	▎	Input: nums = [1,2,2]
	▎	Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

󰛨 Example 2:

	▎	Input: nums = [0]
	▎	Output: [[],[0]]



 Constraints:

	* 1 <= nums.length <= 10
	* -10 <= nums[i] <= 10








The following is my solution to test:
```
# @leet start
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(idx, subset):
            if(idx == len(nums)):
                res.append(subset[::])
                return
            
            subset.append(nums[idx])
            backtrack(idx+1,subset)
            subset.pop()

            while ((idx+1) < len(nums)) and nums[idx] == nums[idx +1]:
                idx += 1
            backtrack(idx+1, subset)

        backtrack(0,[])
        return res
        
# @leet end
```
