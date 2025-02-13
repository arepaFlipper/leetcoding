class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, next_node = node.prev, node.next
        prev.next, next_node.prev = next_node, prev

    def insert(self, node):
        prev, next_node = self.right.prev, self.right
        prev.next = next_node.prev = node
        node.next, node.prev = next_node, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

def test_lru_cache():
    cache = LRUCache(2)  # Initialize LRU cache with capacity 2
    
    test_cases = [
        {"method": "put", "args": (1, 1), "expected": None},  # cache = {1=1}
        {"method": "put", "args": (2, 2), "expected": None},  # cache = {1=1, 2=2}
        {"method": "get", "args": (1,), "expected": 1},       # cache hit, returns 1
        {"method": "put", "args": (3, 3), "expected": None},  # cache = {1=1, 3=3}, evicts 2
        {"method": "get", "args": (2,), "expected": -1},      # cache miss, returns -1
        {"method": "put", "args": (4, 4), "expected": None},  # cache = {3=3, 4=4}, evicts 1
        {"method": "get", "args": (1,), "expected": -1},      # cache miss, returns -1
        {"method": "get", "args": (3,), "expected": 3},       # cache hit, returns 3
        {"method": "get", "args": (4,), "expected": 4},       # cache hit, returns 4
    ]
    
    for i, test in enumerate(test_cases):
        method = getattr(cache, test["method"])
        result = method(*test["args"])
        
        try:
            assert result == test["expected"], f"Test {i + 1} failed: Expected {test['expected']}, got {result}"
            print(f"Test {i + 1} passed! ✅")
        except Exception as e:
            print(f"Test {i + 1} failed with error: {e} ❌")


# Run tests
if __name__ == "__main__":
    test_lru_cache()

