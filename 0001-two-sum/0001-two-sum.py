class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm: Dict = {}
        for (idx, num) in enumerate(nums):
            diff: int = target - num
            if (diff in hm):
                return [idx, hm[diff]]
            hm[num] = idx

