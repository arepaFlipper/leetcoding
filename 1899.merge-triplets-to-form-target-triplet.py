# @leet start
from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            for idx, value in enumerate(triplet):
                if value == target[idx]:
                    good.add(idx)
        return len(good) == 3

# @leet end
# Test Case 1
triplets_1 = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
target_1 = [2, 7, 5]
expected_output_1 = True

print("Test Case 1:")
output_1 = Solution().mergeTriplets(triplets_1, target_1)
print(f"mergeTriplets({triplets_1}, {target_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
triplets_2 = [[3, 4, 5], [4, 5, 6]]
target_2 = [3, 2, 5]
expected_output_2 = False

print("\nTest Case 2:")
output_2 = Solution().mergeTriplets(triplets_2, target_2)
print(f"mergeTriplets({triplets_2}, {target_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
triplets_3 = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
target_3 = [5, 5, 5]
expected_output_3 = True

print("\nTest Case 3:")
output_3 = Solution().mergeTriplets(triplets_3, target_3)
print(f"mergeTriplets({triplets_3}, {target_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

