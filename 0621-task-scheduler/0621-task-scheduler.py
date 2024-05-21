from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [ -cnt for cnt in count.values()]
        print("🍐 \x1b[1;33;40m max_heap:",max_heap,'\x1b[0m') ## DELETEME:
        heapq.heapify(max_heap)
        print("🚇 \x1b[1;30;43m max_heap:",max_heap,'\x1b[0m') ## DELETEME:

        time = 0
        q = deque()

        while max_heap or q:
            print("🔧 \x1b[1;31;46m max_heap:", max_heap, ', q:', q, '\x1b[0m') ## DELETEME:
            time += 1
            print("😍   \x1b[1;37;41m time:", time,'\x1b[0m' ) ## DELETEME:

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                print("🏹  \x1b[1;30;43m max_heap:",max_heap,'\x1b[0m') ## DELETEME:
                print("🥐   \x1b[1;34;40m cnt:", cnt, ', max_heap: ', max_heap, '\x1b[0m') ## DELETEME:
                if cnt:
                    q.append([cnt,time + n])
                    print("🚗 \x1b[1;32;40m q:", q,'\x1b[0m' ) ## DELETEME:

            if q and q[0][1] == time:
                print("🫘  \x1b[1;30;23m max_heap:", max_heap, ', q:', q, '\x1b[0m') ## DELETEME:
                heapq.heappush(max_heap, q.popleft()[0])
                print("🐘 \x1b[1;30;43m max_heap:", max_heap, ', q:', q, '\x1b[0m') ## DELETEME:

        return time

solution = Solution()
#
# # Test Case 1
# input_tasks_1 = ["A", "A", "A", "B", "B", "B"]
# input_n_1 = 2
# expected_output_1 = 8
# result_1 = solution.leastInterval(input_tasks_1, input_n_1)
#
# print("Test Case 1:")
# print("Input:")
# print("tasks:", input_tasks_1)
# print("n:", input_n_1)
# print("Output:", result_1)
#
# if result_1 == expected_output_1:
#     print("✅ Expected Output")
# else:
#     print("❌ Unexpected Output")
#
# # # Test Case 2
# input_tasks_2 = ["A", "A", "A", "B", "B", "B"]
# input_n_2 = 0
# expected_output_2 = 6
# result_2 = solution.leastInterval(input_tasks_2, input_n_2)
#
# print("\nTest Case 2:")
# print("Input:")
# print("tasks:", input_tasks_2)
# print("n:", input_n_2)
# print("Output:", result_2)
#
# if result_2 == expected_output_2:
#     print("✅ Expected Output")
# else:
#     print("❌ Unexpected Output")
#
# # # Test Case 3
# input_tasks_3 = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
# input_n_3 = 2
# expected_output_3 = 16
# result_3 = solution.leastInterval(input_tasks_3, input_n_3)
#
# print("\nTest Case 3:")
# print("Input:")
# print("tasks:", input_tasks_3)
# print("n:", input_n_3)
# print("Output:", result_3)
#
# if result_3 == expected_output_3:
#     print("✅ Expected Output")
# else:
#     print("❌ Unexpected Output")

# Test Case 4
input_tasks_4 = ["A", "A", "A", "B", "B", "C", "C"]
input_n_4 = 1
expected_output_4 = 7
result_4 = solution.leastInterval(input_tasks_4, input_n_4)

print("Test Case 4:")
print("Input:")
print("tasks:", input_tasks_4)
print("n:", input_n_4)
print("Output:", result_4)

if result_4 == expected_output_4:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
