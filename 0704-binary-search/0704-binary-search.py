class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1

        while (left <= right):
            medium = (left + right) // 2
            if (nums[medium] == target):
                return medium
            elif nums[medium]> target:
                right = medium -1
            elif nums[medium]< target:
                left = medium +1
        return -1
