# @leet start
from typing import List

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
    
    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        self.parent[yr] = xr
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indexed_edges = [edge + [i] for i, edge in enumerate(edges)]
        indexed_edges.sort(key=lambda x: x[2])  # sort by weight

        def kruskal(edges_to_use, n, exclude=-1, include=None):
            uf = UnionFind(n)
            weight = 0
            if include is not None:
                if uf.union(include[0], include[1]):
                    weight += include[2]
            for u, v, w, idx in edges_to_use:
                if idx == exclude:
                    continue
                if uf.union(u, v):
                    weight += w
            roots = {uf.find(i) for i in range(n)}
            return weight if len(roots) == 1 else float('inf')

        min_weight = kruskal(indexed_edges, n)
        critical = []
        pseudo_critical = []

        for u, v, w, idx in indexed_edges:
            if kruskal(indexed_edges, n, exclude=idx) > min_weight:
                critical.append(idx)
            elif kruskal(indexed_edges, n, include=[u, v, w, idx]) == min_weight:
                pseudo_critical.append(idx)

        return [critical, pseudo_critical]
# @leet end


# ---------- Vanilla test suite ----------
test_cases = [
    # Test Case 1
    (
        5,                                      # n
        [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]],  # edges
        [[0,1],[2,3,4,5]]                       # expected output
    ),
    # Test Case 2
    (
        4,
        [[0,1,1],[1,2,1],[2,3,1],[0,3,1]],
        [[],[0,1,2,3]]
    ),
]

for idx, (n, edges, expected) in enumerate(test_cases, start=1):
    print(f"\nTest Case {idx}:")
    output = Solution().findCriticalAndPseudoCriticalEdges(n, edges)
    print(f"findCriticalAndPseudoCriticalEdges(n={n}, edges={edges}) => Output:", output)
    if sorted([sorted(x) for x in output]) == sorted([sorted(x) for x in expected]):
        print("✅ Expected Output")
    else:
        print(f"❌ Unexpected Output (expected {expected})")

