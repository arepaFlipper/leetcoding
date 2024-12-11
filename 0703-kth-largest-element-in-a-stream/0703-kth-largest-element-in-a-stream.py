from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        (self.min_heap, self.k) = (nums, k)
        heapq.heapify(nums)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        
    def add(self, val: int) -> int:
        print("""🤖   \x1b[1;33;40m0703-kth-largest-element-in-a-stream.py:12   val:""") ## DELETEME:
        print(val) ## DELETEME:
        print('\x1b[0m') ## DELETEME:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


kth_largest = KthLargest(3, [4, 5, 8, 2])

# Test Case 1
add_1 = kth_largest.add(3)
print("""🟪   \x1b[1;33;40m0703-kth-largest-element-in-a-stream.py:25   kth_largest:""") ## DELETEME:
print(kth_largest.min_heap) ## DELETEME:
print('\x1b[0m') ## DELETEME:
expected_output_1 = 4

print("Test Case 1:")
print("add(3) => Output:", add_1)

if add_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
add_2 = kth_largest.add(5)
print("""🌚   \x1b[1;34;40m0703-kth-largest-element-in-a-stream.py:40   kth_largest.min_heap:""") ## DELETEME:
print(kth_largest.min_heap) ## DELETEME:
print('\x1b[0m') ## DELETEME:
expected_output_2 = 5

print("\nTest Case 2:")
print("add(5) => Output:", add_2)

if add_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
add_3 = kth_largest.add(10)
print("""🏥   \x1b[1;35;40m0703-kth-largest-element-in-a-stream.py:55   kth_largest.min_heap:""") ## DELETEME:
print(kth_largest.min_heap) ## DELETEME:
print('\x1b[0m') ## DELETEME:
expected_output_3 = 5

print("\nTest Case 3:")
print("add(10) => Output:", add_3)

if add_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 4
add_4 = kth_largest.add(9)
print("""💞   \x1b[1;36;40m0703-kth-largest-element-in-a-stream.py:73   kth_largest.min_heap:""") ## DELETEME:
print(kth_largest.min_heap) ## DELETEME:
print('\x1b[0m') ## DELETEME:
expected_output_4 = 8

print("\nTest Case 4:")
print("add(9) => Output:", add_4)

if add_4 == expected_output_4:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 5
add_5 = kth_largest.add(4)
print("""🪃   \x1b[1;37;44m0703-kth-largest-element-in-a-stream.py:91   kth_largest.min_heap:""") ## DELETEME:
print(kth_largest.min_heap) ## DELETEME:
print('\x1b[0m') ## DELETEME:
expected_output_5 = 8

print("\nTest Case 5:")
print("add(4) => Output:", add_5)

if add_5 == expected_output_5:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
