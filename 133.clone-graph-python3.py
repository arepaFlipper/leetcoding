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

# @leet end

def test_clone_graph():
    test_cases = [
        # Test 1: Basic case with 4 nodes (Example 1)
        {
            "adj_list": [[2, 4], [1, 3], [2, 4], [1, 3]],
            "expected": [[2, 4], [1, 3], [2, 4], [1, 3]]
        },

        # Test 2: Single node with no neighbors
        {
            "adj_list": [[]],
            "expected": [[]]
        },

        # Test 3: Empty graph (no nodes)
        {
            "adj_list": [],
            "expected": []
        },

        # Test 4: Two connected nodes
        {
            "adj_list": [[2], [1]],
            "expected": [[2], [1]]
        },

        # Test 5: Three nodes forming a triangle
        {
            "adj_list": [[2, 3], [1, 3], [1, 2]],
            "expected": [[2, 3], [1, 3], [1, 2]]
        },

        # Test 6: Linearly connected nodes (chain)
        {
            "adj_list": [[2], [1, 3], [2, 4], [3]],
            "expected": [[2], [1, 3], [2, 4], [3]]
        }
    ]

    for i, test in enumerate(test_cases):
        original_graph = build_graph(test["adj_list"])  # Convert adjacency list to graph
        cloned_graph = Solution().cloneGraph(original_graph)  # Call your clone function
        cloned_adj_list = graph_to_adj_list(cloned_graph)  # Convert back to adjacency list

        try:
            assert cloned_adj_list == test["expected"], f"Test {i+1} failed: Expected {test['expected']}, got {cloned_adj_list}"
            print(f"Test {i+1} passed! ✅")
        except Exception as e:
            print(f"Test {i+1} failed with error: {e} ❌")


def build_graph(adj_list):
    """Helper function to build a graph from an adjacency list."""
    if not adj_list:
        return None

    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]

    return nodes[1]


def graph_to_adj_list(node):
    """Helper function to convert a graph back into an adjacency list."""
    if not node:
        return []

    visited = {}
    queue = [node]

    while queue:
        curr = queue.pop(0)
        if curr.val not in visited:
            visited[curr.val] = [neighbor.val for neighbor in curr.neighbors]
            for neighbor in curr.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)

    return [visited[i] if i in visited else [] for i in range(1, len(visited) + 1)]


# Run tests
if __name__ == "__main__":
    test_clone_graph()

