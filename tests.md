I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

                https://leetcode.com/problems/single-number/
                                      
                             136. Single Number
                    Easy | 15995  680  | 72.4% of 3.6M



Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



󰛨 Example 1:

	▎ Input: nums = [2,2,1]
	▎ Output: 1

󰛨 Example 2:

	▎ Input: nums = [4,1,2,1,2]
	▎ Output: 4

󰛨 Example 3:

	▎ Input: nums = [1]
	▎ Output: 1



 Constraints:

	* 1 <= nums.length <= 3 * 10^4
	
	* -3 * 10^4 <= nums[i] <= 3 * 10^4
	
	* Each element in the array appears twice except for one element which appears only once.






The following is my solution to test:

```
# @leet start
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
        
# @leet end
```
