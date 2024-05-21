# @leet start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str: str = ""

        for char in s:
            if char.isalnum():
                new_str += char.lower()
        return new_str == new_str[::-1]
        
# @leet end
