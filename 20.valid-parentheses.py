from typing import List
# @leet start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        for char in s:
            if char in pairs.keys():
                stack.append(char)
            else:
                if char == ")":
                    last_char = stack.pop()
                    if last_char != "(":
                        return False
                elif char == "]":
                    last_char = stack.pop()
                    if last_char != "[":
                        return False
                elif char == "}":
                    last_char = stack.pop()
                    if last_char != "{":
                        return False
        if len(stack) > 0:
            return False
        return True


        

# @leet end
# Test functions

def test_valid_parentheses_case_1():
    solution = Solution()
    input_str = "()"
    expected = True
    result = solution.isValid(input_str)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 1 succeed 👍")

def test_valid_parentheses_case_2():
    solution = Solution()
    input_str = "()[]{}"
    expected = True
    result = solution.isValid(input_str)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 2 succeed 👍")

def test_valid_parentheses_case_3():
    solution = Solution()
    input_str = "(]"
    expected = False
    result = solution.isValid(input_str)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 3 succeed 👍")

def test_valid_parentheses_case_4():
    solution = Solution()
    input_str = "([{}])"
    expected = True
    result = solution.isValid(input_str)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 4 succeed 👍")

def test_valid_parentheses_case_5():
    solution = Solution()
    input_str = "([{])}"
    expected = False
    result = solution.isValid(input_str)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 5 succeed 👍")

def main():
    # Simulate running tests
    test_valid_parentheses_case_1()
    test_valid_parentheses_case_2()
    test_valid_parentheses_case_3()
    test_valid_parentheses_case_4()
    test_valid_parentheses_case_5()

if __name__ == "__main__":
    main()
