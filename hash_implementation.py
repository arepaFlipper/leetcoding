class Pair:
  def __init__(self, key, value):
    self.key = key
    self.value = value

class HashMap:
  def __init__(self):
    self.size = 0
    self.capacity = 2
    self.map = [None, None]

  def hash(self, key):
    index = 0
    for char in key:
      index += ord(char)
    return index % self.capacity

  def get(self, key):
    index = self.hash(key)

    while self.map[index] != None:
      if self.map[index].key == key:
        return self.map[index].value
      index += 1
      index = index % self.capacity
    return None


  def rehash(self):
    self.capacity *= 2
    new_map = []
    for idx in range(self.capacity):
      new_map.append(None)

    old_map = self.map
    self.map = new_map
    self.size = 0
    for pair in old_map:
      if pair:
        self.put(pair.key, pair.value)

  def put(self, key, val):
    i = self.hash(key)
    while True:
      if self.map[i] == None:
        self.map[i] = Pair(key, val)
        self.size += 1
        if self.size >= self.capacity // 2:
          self.rehash()
        return
      elif self.map[i].key == key:
        self.map[i].value = val
        return
      
      index += 1
      index = index % self.capacity

  def remove(self, key):
    if not self.get(key):
      return

    index = self.hash(key)
    while True:
      if self.map[index].key == key:
        self.map[index] = None
        self.size -= 1
        return
      index += 1
      index = index % self.capacity

  def print(self):
    for pair in self.map:
      if pair:
        print(pair.key, pair.value)

def test_hash_map():
    hash_map = HashMap()

    test_cases = [
        # Test 1: Insert a key-value pair and retrieve it
        {"method": "put", "args": ("apple", 10), "expected": None},
        {"method": "get", "args": ("apple",), "expected": 10},
        
        # Test 2: Insert another key-value pair and retrieve it
        {"method": "put", "args": ("banana", 20), "expected": None},
        {"method": "get", "args": ("banana",), "expected": 20},

        # Test 3: Update an existing key and retrieve the new value
        {"method": "put", "args": ("apple", 15), "expected": None},
        {"method": "get", "args": ("apple",), "expected": 15},

        # Test 4: Try to retrieve a non-existent key
        {"method": "get", "args": ("grape",), "expected": None},

        # Test 5: Remove an existing key and check if it’s deleted
        {"method": "remove", "args": ("banana",), "expected": None},
        {"method": "get", "args": ("banana",), "expected": None},

        # Test 6: Insert multiple keys to trigger rehashing
        {"method": "put", "args": ("cherry", 30), "expected": None},
        {"method": "put", "args": ("date", 40), "expected": None},
        {"method": "put", "args": ("elderberry", 50), "expected": None},

        # Ensure all elements are still retrievable after rehashing
        {"method": "get", "args": ("apple",), "expected": 15},
        {"method": "get", "args": ("cherry",), "expected": 30},
        {"method": "get", "args": ("date",), "expected": 40},
        {"method": "get", "args": ("elderberry",), "expected": 50},
    ]

    for i, test in enumerate(test_cases):
        method = getattr(hash_map, test["method"])
        result = method(*test["args"])

        try:
            assert result == test["expected"], f"Test {i + 1} failed: Expected {test['expected']}, got {result}"
            print(f"Test {i + 1} passed! ✅")
        except Exception as e:
            print(f"Test {i + 1} failed with error: {e} ❌")


# Run tests
if __name__ == "__main__":
    test_hash_map()

