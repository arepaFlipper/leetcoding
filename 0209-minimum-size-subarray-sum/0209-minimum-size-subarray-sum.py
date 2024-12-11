class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        res = 9e9
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                cur = right - left +1
                res = min(cur, res)
                total -= nums[left]
                left += 1

        if res == 9e9:
            return 0
        else:
            return res
