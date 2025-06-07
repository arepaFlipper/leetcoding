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

# Define test cases as (times, n, k, expected_output)
test_cases = [
    ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
    ([[1, 2, 1]], 2, 1, 1),
    ([[1, 2, 1]], 2, 2, -1),
]

# Run the test cases
for idx, (times, n, k, expected) in enumerate(test_cases, 1):
    print(f"\nTest Case {idx}:")
    output = Solution().networkDelayTime(times, n, k)
    print(f"networkDelayTime({times}, {n}, {k}) => Output:", output)
    if output == expected:
        print("✅ Expected Output")
    else:
        print(f"❌ Unexpected Output (Expected: {expected})")
