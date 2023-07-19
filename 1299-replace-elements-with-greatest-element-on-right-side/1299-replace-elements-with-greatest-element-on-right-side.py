class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0 for el in arr]
        for i, idx in enumerate(arr):
            greatest = -1
            cur_sub = arr[i:]
            for j in range(len(cur_sub)):
                cur= cur_sub[j]
                if cur > greatest:
                    greatest = cur
                ans[j] = greatest
        
        return ans
