# @leet start
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_cp = nums.copy()
        for num in nums_cp:
            nums.append(num)
        return nums
        
# @leet end
