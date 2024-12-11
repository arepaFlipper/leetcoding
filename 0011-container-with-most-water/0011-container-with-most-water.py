class Solution:
    def maxArea(self, height: List[int]) -> int:
        res: int = 0
        l_idx: int = 0
        r_idx: int = len(height)-1
        while l_idx < r_idx:
            h_left = height[l_idx]
            h_right = height[r_idx]
            min_h = min(h_left,h_right)
            width = r_idx - l_idx
            area = min_h * width
            res = max(res,area)
            if h_left < h_right:
                l_idx += 1
            elif h_left >= h_right:
                r_idx -= 1

        return res
