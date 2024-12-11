# @leet start
from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range((len(edges) +1))]
        rank = [1] * (len(edges) +1)
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1, n2):
            (p1, p2) = (find(n1), find(n2))

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1,n2):
                return (n1,n2)
        
# @leet end
# Test Case 1
edges_1 = [[1, 2], [1, 3], [2, 3]]
expected_output_1 = (2, 3)

print("Test Case 1:")
solution_instance = Solution()
output_1 = solution_instance.findRedundantConnection(edges_1)
print(f"findRedundantConnection({edges_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
edges_2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
expected_output_2 = (1, 4)

print("\nTest Case 2:")
solution_instance = Solution()
output_2 = solution_instance.findRedundantConnection(edges_2)
print(f"findRedundantConnection({edges_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

