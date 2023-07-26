class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        print("numSet:",numSet) ## DELETEME:
        longest = 0
        for n in nums:
            if (n-1) not in nums:
                length = 0
                while (n+length) in nums:
                    length += 1
                if length > longest:
                    longest = length
        return longest
