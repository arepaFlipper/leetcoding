# @leet start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets: List = []
        length = len(nums)
        current_subset = []
        def depth_first_search(index):
            if index >= length:
                # WARN: Here is the base case where it hits a leaf.
                subsets.append(current_subset.copy())
                return

            # NOTE: decision to include nums[index]
            num = nums[index]
            current_subset.append(num)
            depth_first_search(index + 1)

            # BUG: decision NOT to include nums[index]
            current_subset.pop()
            depth_first_search(index + 1)

            
        depth_first_search(0)
        return subsets
            
        
# @leet end
