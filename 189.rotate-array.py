# @leet start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)

        for idx in range(k):
            last = nums.pop()
            nums.insert(0,last)
        
# @leet end
