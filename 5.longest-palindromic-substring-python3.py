# @leet start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        print("""\x1b[1;33;40m s: """ , s) ## DELETEME:
        print('\x1b[0m') ## DELETEME:
        res = ""
        res_len = 0

        for idx in range(len(s)):
            print("idx: " , idx) ## DELETEME:
            (left, right) = (idx, idx)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                print("(idx,idx) 👈 \n")
                print("⬅️  left: ", left,", ➡️  right: ", right, "\n") ## DELETEME:
                if (right - left + 1 ) > res_len:
                    res = s[left: right + 1]
                    res_len = right - left + 1
                    print("💍 res: ",res, ", res_len: ", res_len,) 
                left -= 1
                right += 1

            (left, right) = (idx, idx + 1)
            while left >=0 and right < len(s) and s[left] == s[right]:
                print("(idx, idx + 1) 🫵\n")
                print("↙️  left: ", left,", ↘️  right: ", right, "\n") ## DELETEME:
                if (right - left + 1) > res_len:
                    res = s[left : right +1 ]
                    res_len = right - left + 1
                    print("res: ",res, ", res_len: ", res_len, "\n") 
                left -= 1
                right += 1

        return res
# @leet end


# Test functions
def test_longest_palindrome_case_1():
    solution = Solution()
    s = "babad"
    expected = "bab"
    result = solution.longestPalindrome(s)
    assert result == expected or result == "aba", f"Expected {expected} or 'aba', but got {result}"
    print("res: ", result," Case 1 passed ✅")

def test_longest_palindrome_case_2():
    solution = Solution()
    s = "cbbd"
    expected = "bb"
    result = solution.longestPalindrome(s)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("res: ", result," Case 2 passed ✅")

def test_longest_palindrome_case_3():
    solution = Solution()
    s = "a"
    expected = "a"
    result = solution.longestPalindrome(s)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("res: ", result," Case 3 passed ✅")

def test_longest_palindrome_case_4():
    solution = Solution()
    s = "ac"
    expected = "a"
    result = solution.longestPalindrome(s)
    assert result == expected or result == "c", f"Expected {expected} or 'c', but got {result}"
    print("res: ", result," Case 4 passed ✅")

def test_longest_palindrome_case_5():
    solution = Solution()
    s = "racecar"
    expected = "racecar"
    result = solution.longestPalindrome(s)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("res: ", result," Case 5 passed ✅")

def test_longest_palindrome_case_6():
    solution = Solution()
    s = "abcdeffedcba"
    expected = "abcdeffedcba"
    result = solution.longestPalindrome(s)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("res: ", result," Case 6 passed ✅")

def main():
    # Run test cases
    test_longest_palindrome_case_1()
    test_longest_palindrome_case_2()
    test_longest_palindrome_case_3()
    test_longest_palindrome_case_4()
    test_longest_palindrome_case_5()
    test_longest_palindrome_case_6()

if __name__ == "__main__":
    main()
