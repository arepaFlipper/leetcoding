class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        current_r: int = 0
        best_r: int = 0
        for i in range(len(nums)):
            if i == 0 or nums[i-1] >= nums[i]:
                current_r = 1
            else:
                current_r += 1
            best_r = max(best_r, current_r)
        return best_r
