# @leet start
class Solution:
    def rob(self, nums: List[int]) -> int:
        (rob1, rob2) = (0,0)

        for house in nums:
            tmp = max(house + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2
         
# @leet end
