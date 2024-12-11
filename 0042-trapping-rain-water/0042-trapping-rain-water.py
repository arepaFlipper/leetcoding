class Solution:
    def trap(self, height: List[int]) -> int:
        res: int = 0
        if not height:
            return res
        
        l_idx = 0
        r_idx = len(height)-1

        max_l = height[l_idx]
        max_r = height[r_idx]
        while l_idx < r_idx:
            if max_l < max_r:
                l_idx += 1
                max_l = max(max_l, height[l_idx])
                trapped = max_l - height[l_idx]
                res += trapped
            else:
                r_idx -= 1
                max_r = max(max_r, height[r_idx])
                trapped = max_r - height[r_idx]
                res += trapped
        return res
