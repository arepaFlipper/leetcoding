class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        (l,r)=(1,len(numbers))
        while l<r:
            sum = numbers[l-1] + numbers[r-1]
            if sum == target:
                return [l,r]
            elif sum> target:
                r -= 1
            elif sum<target:
                l += 1
