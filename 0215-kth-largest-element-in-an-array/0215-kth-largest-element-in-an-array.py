from typing import List
import heapq

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]

solution = Solution()

def test_find_kth_largest():
    test_cases = [
        {
            "input": {"nums": [3, 2, 1, 5, 6, 4], "k": 2},
            "expected": 5,
        },
        {
            "input": {"nums": [3, 2, 3, 1, 2, 4, 5, 5, 6], "k": 4},
            "expected": 4,
        },
        {
            "input": {"nums": [1], "k": 1},  # Single element case
            "expected": 1,
        },
        {
            "input": {"nums": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], "k": 5},
            "expected": 6,  # Sorted in descending order
        },
        {
            "input": {"nums": [-1, -2, -3, -4, -5], "k": 2},
            "expected": -2,  # All negative numbers
        },
        {
            "input": {"nums": [100, 99, 98, 97, 96], "k": 1},
            "expected": 100,  # k = 1 should return max element
        },
        {
            "input": {"nums": [2, 2, 2, 2, 2], "k": 3},
            "expected": 2,  # All elements are the same
        },
    ]

# Test Case 1
input_nums_1 = [3, 2, 1, 5, 6, 4]
input_k_1 = 2
expected_output_1 = 5
result_1 = solution.findKthLargest(input_nums_1, input_k_1)

print("Test Case 1:")
print("Input:")
print("nums:", input_nums_1)
print("k:", input_k_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_nums_2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
input_k_2 = 4
expected_output_2 = 4
result_2 = solution.findKthLargest(input_nums_2, input_k_2)

print("\nTest Case 2:")
print("Input:")
print("nums:", input_nums_2)
print("k:", input_k_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
# Test Case 1
input_nums_1 = [3, 2, 1, 5, 6, 4]
input_k_1 = 2
expected_output_1 = 5
result_1 = solution.findKthLargest(input_nums_1, input_k_1)

print("Test Case 1:")
print("Input:")
print("nums:", input_nums_1)
print("k:", input_k_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_nums_2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
input_k_2 = 4
expected_output_2 = 4
result_2 = solution.findKthLargest(input_nums_2, input_k_2)

print("\nTest Case 2:")
print("Input:")
print("nums:", input_nums_2)
print("k:", input_k_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

    for i, test in enumerate(test_cases):
        result = find_kth_largest(**test["input"])

        try:
            assert result == test["expected"], f"Test {i + 1} failed: Expected {test['expected']}, got {result}"
            print(f"Test {i + 1} passed! ✅")
        except Exception as e:
            print(f"Test {i + 1} failed with error: {e} ❌")


# Run tests
if __name__ == "__main__":
    test_find_kth_largest()

