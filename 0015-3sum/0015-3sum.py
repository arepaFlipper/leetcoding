class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        nums.sort()
        print("nums:",nums) ## DELETEME:
        for (idx,val) in enumerate(nums):
            if idx > 0 and val == nums[idx-1]:
                continue

            l: int = idx + 1
            r: int = len(nums)-1
            cur_triplet = []
            while l <r:
                sum = val + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                elif sum == 0:
                    print(nums[idx],"+",nums[l],"+",nums[r],"=",sum) ## DELETEME:
                    res.append([val,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res
