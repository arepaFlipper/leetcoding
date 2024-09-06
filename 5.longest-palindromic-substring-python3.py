# @leet start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        longest_len = len (longest_palindrome)

        def expandAroundCenter(start: int, end: int):
            nonlocal longest_palindrome, longest_len
            while (0 <= start) and (end < len(s)) and s[start] == s[end]:
                if( end - start + 1) > longest_len:
                    longest_palindrome = s[start: end + 1]
                    longest_len = end - start + 1
                start = start - 1
                end = end + 1

        for idx in range(len(s)):
            # even
            expandAroundCenter(idx, idx)
            expandAroundCenter(idx, idx+1)
            # odd

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

def test_longest_palindrome_case_7():
    solution = Solution()
    s = "jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"
    expected = "sknks"
    result = solution.longestPalindrome(s)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 7 succeed 👍")


def main():
    # Simulate running tests
    test_longest_palindrome_case_7()
    test_longest_palindrome_case_6()
    test_longest_palindrome_case_1()
    test_longest_palindrome_case_2()
    test_longest_palindrome_case_3()
    test_longest_palindrome_case_4()
    test_longest_palindrome_case_5()

if __name__ == "__main__":
    main()
