# @leet start
from typing import List
from collections import defaultdict
class DetectSquares:

    def __init__(self):
        self.pts_count = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.pts_count[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        (px, py) = point
        for x,y in self.pts:
            if (abs(py-y) != abs(px-x)) or (x == px or y == py):
                continue
            res += self.pts_count[(x,py)] * self.pts_count[(px,y)]
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @leet end
# Test Case 1
detect_squares_1 = DetectSquares()
detect_squares_1.add([3, 10])
detect_squares_1.add([11, 2])
detect_squares_1.add([3, 2])
output_1_1 = detect_squares_1.count([11, 10])
expected_output_1_1 = 1
print("Test Case 1.1:")
print(f"count([11, 10]) => Output: {output_1_1}")
if output_1_1 == expected_output_1_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

output_1_2 = detect_squares_1.count([14, 8])
expected_output_1_2 = 0
print("\nTest Case 1.2:")
print(f"count([14, 8]) => Output: {output_1_2}")
if output_1_2 == expected_output_1_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

detect_squares_1.add([11, 2])
output_1_3 = detect_squares_1.count([11, 10])
expected_output_1_3 = 2
print("\nTest Case 1.3:")
print(f"count([11, 10]) => Output: {output_1_3}")
if output_1_3 == expected_output_1_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

