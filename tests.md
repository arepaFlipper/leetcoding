I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

                https://leetcode.com/problems/contains-duplicate/
                                        
                             217. Contains Duplicate
                     Easy  │ 11801  1287  │ 61.7% of 6.4M



Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



󰛨 Example 1:

	│ Input: nums = [1,2,3,1]
	│ Output: true

󰛨 Example 2:

	│ Input: nums = [1,2,3,4]
	│ Output: false

󰛨 Example 3:

	│ Input: nums = [1,1,1,3,3,4,3,2,4,2]
	│ Output: true



 Constraints:

	* 1 <= nums.length <= 10^5
	
	* -10^9 <= nums[i] <= 10^9





The following is my solution to test:

```py
from typing import List

# @leet start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
# @leet end
```
