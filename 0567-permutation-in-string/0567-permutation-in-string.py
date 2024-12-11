class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count, s2_count = [0] * 26, [0]*26

        for i in range(len(s1)):
            s1_count[ord(s1[i])- ord ('a')] += 1
            s2_count[ord(s2[i])- ord ('a')] += 1
            print("s1_count:",s1_count) ## DELETEME:
            print("s2_count:",s2_count) ## DELETEME:
        
        matches = 0

        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
        print("matches:",matches) ## DELETEME:

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1

            if s1_count[index] == s2_count[index]:
                matches +=1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2_count[index] -=1

            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] -1 == s2_count[index]:
                matches -= 1
            l += 1

        return matches == 26
# Test the function
solution = Solution()
# s1 = "ab"
# s2 = "eidbaooo"
# result = solution.checkInclusion(s1, s2)
s1 = "abc"
s2 = "baxyzabc"
result = solution.checkInclusion(s1, s2)

if result:
    print(f'"{s1}" is a permutation of "{s2}"')
else:
    print(f'"{s1}" is not a permutation of "{s2}"')
