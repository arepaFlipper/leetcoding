class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: List = [] ## (idx,height)
        max_area: int = 0
        for idx, h in enumerate(heights):
            start = idx
            while (len(stack)>0) and (stack[-1][1]>h):
                (jdx,cur_h) = stack.pop()
                width = idx - jdx
                cur_area = width*cur_h
                max_area = max(max_area,cur_area)
                start = jdx
            stack.append((start,h))

        total_w = len(heights)
        for idx, h in stack:
            width = total_w - idx 
            cur_area = h*width
            max_area = max(max_area, cur_area)
        return max_area
