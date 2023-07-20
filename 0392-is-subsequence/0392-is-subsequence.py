class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx= 0
        for c in s:
            if c in t:
                idx = t.index(c)
            else:
                return False
            idx += 1
            t = t[idx:]
        return True

if __name__ == '__main__':
    solution = Solution()
    
    # Test Cases
    print("Test Case 1:", solution.isSubsequence("twn", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn"))
    print("Test Case 2:", solution.isSubsequence("aaaaaa", "bbaaaa"))
    print("Test Case 3:", solution.isSubsequence("abc", "ahbgdc"))
    print("Test Case 4:", solution.isSubsequence("axc", "ahbgdc"))
