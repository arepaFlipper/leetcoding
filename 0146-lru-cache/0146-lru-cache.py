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

# Test Cases
cache = LRUCache(2)
operations = ["put", "put", "get", "put", "get", "put", "get", "get", "get"]
operands = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
expected_results = [None, None, 1, None, -1, None, -1, 3, 4]

for i in range(len(operations)):
    operation = operations[i]
    operand = operands[i]

    if operation == "put":
        cache.put(operand[0], operand[1])
        print("Operation: put({}, {})".format(operand[0], operand[1]))
    elif operation == "get":
        result = cache.get(operand[0])
        print("Operation: get({})".format(operand[0]))
        print("Result:", result)
        if result == expected_results[i]:
            print("✅ Expected:", expected_results[i])
        else:
            print("❌ Expected:", expected_results[i])
