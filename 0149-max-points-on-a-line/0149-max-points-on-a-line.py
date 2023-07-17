class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 1. For each point determine if it lies on the longest line
        # 2. count all points with same slope
        # 3. Update result with max.
        res =1
        size = len(points)
        for i in range(size):
            p1 = points[i] 
            x1 = p1[0]
            y1 = p1[1]
            count = collections.defaultdict(int)
            for j in range(i+1,size):
                p2 = points[j]
                x2 = p2[0]
                y2 = p2[1]
                delta_x= x2-x1
                delta_y= y2-y1
                if delta_x==0:
                    slope = float("inf")
                else:
                    slope = delta_y/delta_x
                count[slope]+= 1
                res = max(res, count[slope]+ 1)
            
        return res
        

        
