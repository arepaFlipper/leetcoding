class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    def hash_function(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        node = self.table[index]

        # If table entry is empty, insert node
        if not node:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            # If table entry has nodes, check for key update or append to the end
            prev = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)
            self.size += 1

        # Check if resizing is needed
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next

        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        node = self.table[index]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                self.size -= 1
                return True
            prev, node = node, node.next

        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for node in self.table:
            while node:
                index = node.key % new_capacity
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.value)
                else:
                    new_node = new_table[index]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.value)
                node = node.next

        self.capacity = new_capacity
        self.table = new_table

def test_hash_table():
    hash_table = HashTable(4)

    test_cases = [
        # Test 1: Initial capacity
        {"method": "getCapacity", "args": (), "expected": 4},

        # Test 2: Insert a key-value pair and retrieve it
        {"method": "insert", "args": (1, 2), "expected": None},
        {"method": "get", "args": (1,), "expected": 2},

        # Test 3: Update an existing key and retrieve the new value
        {"method": "insert", "args": (1, 3), "expected": None},
        {"method": "get", "args": (1,), "expected": 3},

        # Test 4: Remove an existing key and verify deletion
        {"method": "remove", "args": (1,), "expected": True},
        {"method": "get", "args": (1,), "expected": -1},

        # Test 5: Remove a non-existent key
        {"method": "remove", "args": (2,), "expected": False},

        # Test 6: Insert multiple elements to test capacity growth
        {"method": "insert", "args": (2, 10), "expected": None},
        {"method": "insert", "args": (3, 20), "expected": None},
        {"method": "insert", "args": (4, 30), "expected": None},

        # Test 7: Verify automatic resize after reaching load factor >= 0.5
        {"method": "getCapacity", "args": (), "expected": 8},  # Capacity should double

        # Test 8: Ensure all elements are still retrievable after resize
        {"method": "get", "args": (2,), "expected": 10},
        {"method": "get", "args": (3,), "expected": 20},
        {"method": "get", "args": (4,), "expected": 30},

        # Test 9: Verify size
        {"method": "getSize", "args": (), "expected": 3},

        # Test 10: Further insertions to validate resizing again
        {"method": "insert", "args": (5, 40), "expected": None},
        {"method": "insert", "args": (6, 50), "expected": None},
        {"method": "getCapacity", "args": (), "expected": 16},  # Should resize again

        # Test 11: Ensure correct retrieval after multiple resizes
        {"method": "get", "args": (5,), "expected": 40},
        {"method": "get", "args": (6,), "expected": 50},
    ]

    for i, test in enumerate(test_cases):
        method = getattr(hash_table, test["method"])
        result = method(*test["args"])

        try:
            assert result == test["expected"], f"Test {i + 1} failed: Expected {test['expected']}, got {result}"
            print(f"Test {i + 1} passed! ✅")
        except Exception as e:
            print(f"Test {i + 1} failed with error: {e} ❌")


# Run tests
if __name__ == "__main__":
    test_hash_table()

