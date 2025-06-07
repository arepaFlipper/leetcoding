# @leet start
import heapq
from typing import List, Tuple
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        max_heap = [(-1.0, start)]
        visited = set()

        while max_heap:
            prob, node = heapq.heappop(max_heap)
            prob = -prob
            if node == end:
                return prob
            if node in visited:
                continue
            visited.add(node)
            for neighbor, edge_prob in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(max_heap, (-(prob * edge_prob), neighbor))
        return 0.0
# @leet end


# ---------- Vanilla test suite ----------
test_cases = [
    # Test Case 1
    (
        3,                                      # n
        [[0, 1], [1, 2], [0, 2]],               # edges
        [0.5, 0.5, 0.2],                        # succProb
        0,                                      # start
        2,                                      # end
        0.25                                    # expected
    ),
    # Test Case 2
    (
        3,
        [[0, 1], [1, 2], [0, 2]],
        [0.5, 0.5, 0.3],
        0,
        2,
        0.3
    ),
    # Test Case 3: No path exists
    (
        3,
        [[0, 1]],
        [0.5],
        0,
        2,
        0.0
    ),
]

for idx, (n, edges, succProb, start, end, expected) in enumerate(test_cases, start=1):
    print(f"\nTest Case {idx}:")
    output = Solution().maxProbability(n, edges, succProb, start, end)
    print(f"maxProbability(n={n}, edges={edges}, succProb={succProb}, start={start}, end={end}) => Output:", output)
    if abs(output - expected) < 1e-5:
        print("✅ Expected Output")
    else:
        print(f"❌ Unexpected Output (expected {expected})")

