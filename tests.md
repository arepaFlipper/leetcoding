I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

       https://leetcode.com/problems/min-cost-to-connect-all-points/
                                      
                    1584. Min Cost to Connect All Points
             Medium │ 4892  120  │ 66.6% of 400.4K │ 󰛨 Hints



You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [x_i, y_i].

The cost of connecting two points [x_i, y_i] and [x_j, y_j] is the manhattan distance between them: |x_i - x_j| + |y_i - y_j|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.



󰛨 Example 1:

[img](https://assets.leetcode.com/uploads/2020/08/26/d.png)

	│ Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
	│ Output: 20
	│ Explanation: 
	│ 
	│ [img](https://assets.leetcode.com/uploads/2020/08/26/c.png)
	│ 
	│ We can connect the points as shown above to get the minimum cost of 20.
	│ Notice that there is a unique path between every pair of points.

󰛨 Example 2:

	│ Input: points = [[3,12],[-2,5],[-4,1]]
	│ Output: 18



 Constraints:

	* 1 <= points.length <= 1000
	
	* -10^6 <= x_i, y_i <= 10^6
	
	* All pairs (x_i, y_i) are distinct.







The following is my solution to test:

```
# @leet start
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N: int = len(points)
        adj : Dict = { i: [] for i in range(N) }
        for idx in range(N):
            (x1,y1) = points[idx]
            for jdx in range(idx +1, N):
                (x2,y2) = points[jdx]
                distance = abs(x2 - x1) + abs(y2-y1)
                adj[idx].append([distance,jdx])
                adj[jdx].append([distance,idx])
        res: int = 0
        visit = set()
        min_heap = [[0,0]]
        while len(visit) < N:
            cost, point = heapq.heappop(min_heap)
            if point in visit:
                continue
            res += cost
            visit.add(point)
            for cost_nei, neighbor in adj[point]:
                if neighbor not in visit:
                    heapq.heappush(min_heap,[cost_nei, neighbor])

        return res
# @leet end
```
