class TimeMap:
    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        left = 0
        right = len(values) - 1
        while left <= right:
            med = (left + right) // 2
            if values[med][1] <= timestamp:
                res = values[med][0]
                left = med + 1
            else:
                right = med - 1

        return res

def test_time_based_key_value_store(operations, values):
    timeMap = TimeMap()
    output = []

    for i in range(len(operations)):
        operation = operations[i]
        value = values[i]

        if operation == "set":
            key, val, timestamp = value
            timeMap.set(key, val, timestamp)
            output.append(None)
        elif operation == "get":
            key, timestamp = value
            result = timeMap.get(key, timestamp)
            output.append(result)

    expected = [None, "bar", "bar",None, "bar2", "bar2"]
    print("Input operations:", operations)
    print("Input values:", values)
    print("Output:", output)
    print("Expected:", expected)

    if output == expected:
        print("✅ Test passed")
    else:
        print("❌ Test failed")

# Test case
operations = ["TimeMap", "set", "get", "get", "set", "get", "get"]
values = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

test_time_based_key_value_store(operations, values)

