class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output: List[int] = []

        prefix : int = 1
        for value in (nums):
            output.append(prefix)
            prefix *= value

        postfix : int = 1
        for (idx,val) in reversed(list(enumerate(nums))):
            output[idx]= output[idx] * postfix
            postfix *= val

        return output
