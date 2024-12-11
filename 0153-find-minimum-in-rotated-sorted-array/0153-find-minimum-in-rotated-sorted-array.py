class Solution:
    def findMin(self, nums: List[int]) -> int:
        res: int = nums[0]
        left: int = 0
        right: int = len(nums) - 1

        while (left <= right):
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            med = ( right + left ) // 2
            res = min (res, nums[med])
            if nums[med] >= nums[left]:
                left = med + 1
            else:
                right = med - 1
        return res
