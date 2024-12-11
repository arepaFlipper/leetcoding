# @leet start
from typing import List, Counter, defaultdict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (min(r, c) < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
                return False
            
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


solution = Solution()

# Test Case 1
input_board_1 = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]
input_word_1 = "ABCCED"
expected_output_1 = True
result_1 = solution.exist(input_board_1, input_word_1)

print("Test Case 1:")
print("Input:")
print("Board:", input_board_1)
print("Word:", input_word_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_board_2 = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]
input_word_2 = "SEE"
expected_output_2 = True
result_2 = solution.exist(input_board_2, input_word_2)

print("\nTest Case 2:")
print("Input:")
print("Board:", input_board_2)
print("Word:", input_word_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
input_board_3 = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]
input_word_3 = "ABCB"
expected_output_3 = False
result_3 = solution.exist(input_board_3, input_word_3)

print("\nTest Case 3:")
print("Input:")
print("Board:", input_board_3)
print("Word:", input_word_3)
print("Output:", result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# @leet end
