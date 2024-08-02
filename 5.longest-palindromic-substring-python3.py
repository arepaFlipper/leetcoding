# @leet start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        length = len(s)
        start = 0
        end = start
        while start <= length:
            while end <= length:
                current = s[start:end]
                if current == current[::-1] and len(current)> len(longest_palindrome):
                    longest_palindrome = current
                end = end + 1
            start = start + 1
            end = start

        return longest_palindrome

# @leet end


# Test functions
def test_longest_palindrome_case_6():
    solution = Solution()
    s = "abb"
    expected = "bb"
    result = solution.longestPalindrome(s)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 5 succeed 👍")

def test_longest_palindrome_case_1():
    solution = Solution()
    s = "babad"
    expected = "bab"
    result = solution.longestPalindrome(s)
    assert result == expected or result == "aba", f"Expected {expected} or 'aba', but got {result}"
    print("Case 1 succeed 👍")

def test_longest_palindrome_case_2():
    solution = Solution()
    s = "cbbd"
    expected = "bb"
    result = solution.longestPalindrome(s)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 2 succeed 👍")

def test_longest_palindrome_case_3():
    solution = Solution()
    s = "a"
    expected = "a"
    result = solution.longestPalindrome(s)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 3 succeed 👍")

def test_longest_palindrome_case_4():
    solution = Solution()
    s = "ac"
    expected = "a"
    result = solution.longestPalindrome(s)
    assert result == expected or result == "c", f"Expected {expected} or 'c', but got {result}"
    print("Case 4 succeed 👍")

def test_longest_palindrome_case_5():
    solution = Solution()
    s = "racecar"
    expected = "racecar"
    result = solution.longestPalindrome(s)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 5 succeed 👍")

def main():
    # Simulate running tests
    test_longest_palindrome_case_6()
    test_longest_palindrome_case_1()
    test_longest_palindrome_case_2()
    test_longest_palindrome_case_3()
    test_longest_palindrome_case_4()
    test_longest_palindrome_case_5()

if __name__ == "__main__":
    main()
