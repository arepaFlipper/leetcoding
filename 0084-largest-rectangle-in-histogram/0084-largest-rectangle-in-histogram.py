class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: List = [] # {idx,height}
        max_area: number = 0

        for (idx, h) in enumerate(heights):
            start = idx
            while (len(stack)>0) and stack[-1][1] > h:
                (jdx, cur_h) = stack.pop()
                width = idx - jdx
                vertical_area = width * cur_h
                max_area = max(max_area,vertical_area)
                start = jdx
            stack.append((start,h))

        print("stack:",stack) ## DELETEME:
        total_w = len(heights)

        for (jdx, h) in stack:
            width = total_w - jdx
            horizontal_area = h * width
            max_area = max(max_area,horizontal_area)

        return max_area
