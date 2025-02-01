from typing import List

class TreeNode:
    def __init__(self, key: int, val: int):
        self.val = val
        self.key = key
        self.left = None
        self.right = None


class TreeMap:
    def __init__(self):
        """Initialize the BST map."""
        self.root = None

    def insert(self, key: int, val: int) -> None:
        """Insert a key-value pair into the tree, replacing existing key if present."""
        new_node = TreeNode(key, val)
        if not self.root:
            self.root = new_node
            return

        current = self.root
        while current:
            if key < current.key:
                if not current.left:
                    current.left = new_node
                    break
                current = current.left
            elif current.key < key:
                if not current.right:
                    current.right = new_node
                    break
                current = current.right
            else:
                current.val = val
                break

    def get(self, key: int) -> int:
        """Return the value mapped to the given key, or -1 if not found."""
        current = self.root
        while current:
            if key > current.key:
                current = current.right
            elif key < current.key:
                current = current.left
            else:
                return current.val
        return -1

    def getMin(self) -> int:
        """Return the value associated with the smallest key, or -1 if tree is empty."""
        res = self.findMin(self.root)
        return res.val if res else -1

    def findMin(self, root: TreeNode) -> int:
        if not root:
            return None

        current = root
        while current and current.left:
            current = current.left

        return current

    def getMax(self) -> int:
        """Return the value associated with the largest key, or -1 if tree is empty."""
        if not self.root:
            return -1

        current = self.root

        while current and current.right:
            current = current.right

        return current.val

    def remove(self, key: int) -> None:
        """Remove the key-value pair with the given key from the tree."""
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        current = root
        if key > current.key:
            root.right = self.removeHelper(current.right, key)
        elif key < current.key:
            root.left = self.removeHelper(current.left, key)
        else:
            
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.findMin(root.right)
                root.key = min_node.key
                root.val = min_node.val
                root.right = self.removeHelper(root.right, min_node.key)

        return root

    def getInorderKeys(self) -> List[int]:
        """Return an array of keys in the tree in ascending order."""
        res = []
        self.inOrderTraversal(self.root, res)
        return res

    def inOrderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if not root:
            return
        self.inOrderTraversal(root.left, result)
        result.append(root.key)
        self.inOrderTraversal(root.right, result)

def test_tree_map():
    test_cases = [
        # Example 1
        {
            "operations": ["insert", "get", "insert", "getMin", "getMax"],
            "arguments": [[1, 2], [1], [4, 0], [], []],
            "expected": [None, 2, None, 2, 0]
        },

        # Example 2
        {
            "operations": ["insert", "insert", "insert", "insert", "getInorderKeys", "remove", "getInorderKeys"],
            "arguments": [[1, 2], [4, 2], [3, 7], [2, 1], [], [1], []],
            "expected": [None, None, None, None, [1, 2, 3, 4], None, [2, 3, 4]]
        },

        # Additional Test: Empty tree operations
        {
            "operations": ["get", "getMin", "getMax", "getInorderKeys"],
            "arguments": [[10], [], [], []],
            "expected": [-1, -1, -1, []]
        },

        # Additional Test: Insert and overwrite value
        {
            "operations": ["insert", "insert", "get"],
            "arguments": [[5, 10], [5, 20], [5]],
            "expected": [None, None, 20]
        },
        # Additional Test: Remove nonexistent key
        {
            "operations": ["insert", "insert", "remove", "getInorderKeys"],
            "arguments": [[2, 5], [3, 6], [1], []],
            "expected": [None, None, None, [2, 3]]
        }
    ]

    for i, test in enumerate(test_cases):
        tree = TreeMap()
        result = []
        
        try:
            for op, args in zip(test["operations"], test["arguments"]):
                if op == "insert":
                    tree.insert(*args)
                    result.append(None)
                elif op == "get":
                    result.append(tree.get(*args))
                elif op == "getMin":
                    result.append(tree.getMin())
                elif op == "getMax":
                    result.append(tree.getMax())
                elif op == "remove":
                    tree.remove(*args)
                    result.append(None)
                elif op == "getInorderKeys":
                    result.append(tree.getInorderKeys())

            assert result == test["expected"], f"Test case {i + 1} failed: Expected {test['expected']}, got {result}"
            print(f"Test case {i + 1} passed! ✅")
        except Exception as e:
            print(f"Test case {i + 1} failed with error: {e} ❌")

# Run tests
if __name__ == "__main__":
    test_tree_map()

