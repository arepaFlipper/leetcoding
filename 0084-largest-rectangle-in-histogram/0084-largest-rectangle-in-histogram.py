class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: List[tuple(int)] = [] # (idx,height)
        max_area: int = 0

        for idx, h in enumerate(heights):
            start = idx
            while (len(stack)>0) and stack[-1][1] > h:
                (jdx,height) = stack.pop()
                width = idx - jdx
                cur_area = width * height
                max_area = max(max_area,cur_area) 
                start = jdx
            stack.append((start,h))

        total_w = len(heights)

        for (start, height) in (stack):
            cur_area = height*(total_w-start)
            max_area = max(cur_area, max_area)

        return max_area
