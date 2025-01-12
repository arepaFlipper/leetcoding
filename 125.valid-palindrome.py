import re

# @leet start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = self.alphabetic(s)
        print("""🤶   \x1b[1;33;40m125.valid-palindrome.py:7    string:""") ## DELETEME:
        print(string) ## DELETEME:
        print('\x1b[0m') ## DELETEME:
        stack = ""
        for char in string[::-1]:
            stack += char
        
        if stack != string:
            return False
        else:
            return True

    def alphabetic(self, string: str)-> str:
        res = ""
        for char in string:
            dec = ord(char)
            if 65 <= dec and dec <= 90:
                res += chr(dec+ (97 - 65))

            elif 97 <= dec and dec <= 122:
                res += char
        return res

        
# @leet end
# # Test functions
def test_valid_palindrome_case_1():
    solution = Solution()
    input_str = "A man, a plan, a canal: Panama"
    expected = True
    result = solution.isPalindrome(input_str)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 1 succeed 👍")

def test_valid_palindrome_case_2():
    solution = Solution()
    input_str = "race a car"
    expected = False
    result = solution.isPalindrome(input_str)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 2 succeed 👍")

def test_valid_palindrome_case_3():
    solution = Solution()
    input_str = " "
    expected = True
    result = solution.isPalindrome(input_str)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 3 succeed 👍")

def test_valid_palindrome_case_4():
    solution = Solution()
    input_str = "Able was I ere I saw Elba"
    expected = True
    result = solution.isPalindrome(input_str)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 4 succeed 👍")

def test_valid_palindrome_case_5():
    solution = Solution()
    input_str = "No lemon, no melon"
    expected = True
    result = solution.isPalindrome(input_str)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 5 succeed 👍")

def main():
    # Simulate running tests
    test_valid_palindrome_case_1()
    test_valid_palindrome_case_2()
    test_valid_palindrome_case_3()
    test_valid_palindrome_case_4()
    test_valid_palindrome_case_5()

if __name__ == "__main__":
    main()
