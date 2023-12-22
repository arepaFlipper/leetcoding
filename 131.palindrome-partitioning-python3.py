# @leet start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        (res, part) = ([], [])

        def depth_first_search(idx):
            if idx >= len(s):
                res.append(part.copy())
                return
            for jdx in range(idx, len(s)):
                if self.is_pali(s, idx, jdx):
                    part.append(s[idx : jdx +1])
                    depth_first_search(jdx +1)
                    part.pop()

        depth_first_search(0)
        return res
    
    def is_pali(self, string, left, right):
        while left < right:
            if string[left] != string[right]:
                return False
            (left,right) = (left+1, right-1)
        return True
        
# @leet end
