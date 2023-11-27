from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_count = max(counter.values())
        nutshell = sum(map(lambda count: count == max_count, counter.values()))
        min_time = (max_count - 1 ) * (n +1) + nutshell
        
        return max(min_time, len(tasks))

solution = Solution()

# Test Case 1
input_tasks_1 = ["A", "A", "A", "B", "B", "B"]
input_n_1 = 2
expected_output_1 = 8
result_1 = solution.leastInterval(input_tasks_1, input_n_1)

print("Test Case 1:")
print("Input:")
print("tasks:", input_tasks_1)
print("n:", input_n_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_tasks_2 = ["A", "A", "A", "B", "B", "B"]
input_n_2 = 0
expected_output_2 = 6
result_2 = solution.leastInterval(input_tasks_2, input_n_2)

print("\nTest Case 2:")
print("Input:")
print("tasks:", input_tasks_2)
print("n:", input_n_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
input_tasks_3 = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
input_n_3 = 2
expected_output_3 = 16
result_3 = solution.leastInterval(input_tasks_3, input_n_3)

print("\nTest Case 3:")
print("Input:")
print("tasks:", input_tasks_3)
print("n:", input_n_3)
print("Output:", result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
