# @leet start
from typing import List
import heapq

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

# Test Case 1
points_1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
expected_output_1 = 20

print("Test Case 1:")
output_1 = Solution().minCostConnectPoints(points_1)
print(f"minCostConnectPoints({points_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
points_2 = [[3,12],[-2,5],[-4,1]]
expected_output_2 = 18

print("\nTest Case 2:")
output_2 = Solution().minCostConnectPoints(points_2)
print(f"minCostConnectPoints({points_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

