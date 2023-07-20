class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i , j = 0,0
        while (i < len(s)) and (j<len(t)):
            if s[i] == t[j]:
                i += 1
            j += 1

        if i == len(s):
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    
    # Test Cases
    test_1 = solution.isSubsequence("twn", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn")
    print("Test Case 1:", test_1, "✔️ " if test_1 else "❌")

    test_2 = solution.isSubsequence("aaaaaa", "bbaaaa")
    print("Test Case 2:", test_2, "✔️ " if not test_2 else "❌")

    test_3 = solution.isSubsequence("abc", "ahbgdc")
    print("Test Case 3:", test_3, "✔️ " if test_3 else "❌")

    test_4 = solution.isSubsequence("axc", "ahbgdc")
    print("Test Case 4:", test_4, "✔️ " if not test_4 else "❌")
