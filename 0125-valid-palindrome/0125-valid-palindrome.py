class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            while (not self.is_alphanum(s[l]) and l<r):
                l += 1
            while (not self.is_alphanum(s[r]) and l<r):
                r -= 1

            print(s[l], "==", s[r]) ## DELETEME:
            if (s[l].lower()!= s[r].lower()):
                print(s[l], "==", s[r]) ## DELETEME:
                return False
            
            l += 1
            r -= 1
        return True

    def is_alphanum(self, c):
        print('c: ',c) ## DELETEME:
        if (ord('a') <= ord(c) and ord(c)<=ord('z')
                or ord('A')<=ord(c) and ord(c) <=ord('Z')
                or ord('0') <= ord(c) and ord(c)<= ord('9')):
            return True
        return False
        
