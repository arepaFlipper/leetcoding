# @leet start
from typing import Optional, List, Dict

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new: Dict = {}

        def depth_first_search(node):
            if node in old_to_new:
                return old_to_new[node]

            node_copied = Node(node.val)
            old_to_new[node] = node_copied
            for neighbor in node.neighbors:
                node_copied.neighbors.append(depth_first_search(neighbor))
            return node_copied

        return depth_first_search(node) if node else None

solution = Solution()

# Test Case 1
adjList_1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
expected_output_1 = [[2, 4], [1, 3], [2, 4], [1, 3]]

print("Test Case 1:")
graph_1 = Solution().cloneGraph(Node(1, [Node(2), Node(4)]))
output_1 = []
if graph_1:
    visited_1 = set()

    def traverse(node):
        if node.val not in visited_1:
            visited_1.add(node.val)
            output_1.append([neighbor.val for neighbor in node.neighbors])
            for neighbor in node.neighbors:
                traverse(neighbor)

    traverse(graph_1)

print(f"cloneGraph({adjList_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
adjList_2 = [[]]
expected_output_2 = [[]]

print("\nTest Case 2:")
graph_2 = Solution().cloneGraph(Node(1, []))
output_2 = []
if graph_2:
    visited_2 = set()

    def traverse(node):
        if node.val not in visited_2:
            visited_2.add(node.val)
            output_2.append([neighbor.val for neighbor in node.neighbors])
            for neighbor in node.neighbors:
                traverse(neighbor)

    traverse(graph_2)

print(f"cloneGraph({adjList_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
adjList_3 = []
expected_output_3 = []

print("\nTest Case 3:")
graph_3 = Solution().cloneGraph(None)
output_3 = []
if graph_3:
    visited_3 = set()

    def traverse(node):
        if node.val not in visited_3:
            visited_3.add(node.val)
            output_3.append([neighbor.val for neighbor in node.neighbors])
            for neighbor in node.neighbors:
                traverse(neighbor)

    traverse(graph_3)

print(f"cloneGraph({adjList_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

