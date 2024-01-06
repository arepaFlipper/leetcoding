I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

https://leetcode.com/problems/maximum-product-subarray/
                        
          152. Maximum Product Subarray
     Medium | 17848  568  | 34.9% of 3.3M



Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



󰛨 Example 1:

	▎	Input: nums = [2,3,-2,4]
	▎	Output: 6
	▎	Explanation: [2,3] has the largest product 6.

󰛨 Example 2:

	▎	Input: nums = [-2,0,-1]
	▎	Output: 0
	▎	Explanation: The result cannot be 2, because [-2,-1] is not a subarray.



 Constraints:

	* 1 <= nums.length <= 2 * 10^4
	
	* -10 <= nums[i] <= 10
	
	* The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.









The following is my solution to test:
```

# @leet start

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res: int = nums[0]
        (current_min,current_max) = (1,1)

        for number in nums:
            temp = current_max * number
            current_max=max(number,temp,current_min*number)
            current_min = min(temp,current_min*number, number)
            res = max(res,current_max)
        return res
# @leet end
        
```
