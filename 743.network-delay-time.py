# @leet start
import collections, heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for (u,v,w) in times:
            edges[u].append((v,w))

        min_heap = [(0,k)]
        visit = set()
        t = 0
        while min_heap:
            (w1,n1) = heapq.heappop(min_heap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for (n2,w2) in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(min_heap, (w1+w2,n2))

        return t if len(visit) == n else -1
        
# @leet end
#
# Test Case 1
times_1 = [[2,1,1],[2,3,1],[3,4,1]]
n_1 = 4
k_1 = 2
expected_output_1 = 2

print("Test Case 1:")
output_1 = Solution().networkDelayTime(times_1, n_1, k_1)
print(f"networkDelayTime({times_1}, {n_1}, {k_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
times_2 = [[1,2,1]]
n_2 = 2
k_2 = 1
expected_output_2 = 1

print("\nTest Case 2:")
output_2 = Solution().networkDelayTime(times_2, n_2, k_2)
print(f"networkDelayTime({times_2}, {n_2}, {k_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
times_3 = [[1,2,1]]
n_3 = 2
k_3 = 2
expected_output_3 = -1

print("\nTest Case 3:")
output_3 = Solution().networkDelayTime(times_3, n_3, k_3)
print(f"networkDelayTime({times_3}, {n_3}, {k_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

