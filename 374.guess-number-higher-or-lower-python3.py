# Mocking the guess API for testing
class MockGuessAPI:
    def __init__(self, pick: int):
        self.pick = pick

    def guess(self, num: int) -> int:
        if num > self.pick:
            return -1
        elif num < self.pick:
            return 1
        else:
            return 0

# Your solution class
class Solution:
    def __init__(self, guess_api):
        self.guess_api = guess_api

    def guessNumber(self, n: int) -> int:
        (left, right) = (1, n)
        while left <= right:
            mid = left + (right - left) // 2
            result = self.guess_api.guess(mid)
            if 0 < result:
                left = mid + 1
            elif result < 0:
                right = mid - 1
            else:
                return result
        return -1  # Should never reach here

# Test cases
def test_guess_number():
    test_cases = [
        {"n": 10, "pick": 6, "expected": 6},
        {"n": 1, "pick": 1, "expected": 1},
        {"n": 2, "pick": 1, "expected": 1},
        {"n": 100, "pick": 99, "expected": 99},
        {"n": 1000, "pick": 500, "expected": 500},
    ]

    for i, test in enumerate(test_cases):
        mock_api = MockGuessAPI(test["pick"])
        solution = Solution(mock_api)
        result = solution.guessNumber(test["n"])
        assert result == test["expected"], f"Test case {i+1} failed: {result} != {test['expected']}"
        print(f"Test case {i+1} passed!")

# Run the tests
test_guess_number()

