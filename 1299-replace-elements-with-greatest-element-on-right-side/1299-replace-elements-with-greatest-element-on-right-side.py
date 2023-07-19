# !/usr/bin/env python
from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        for j in range(len(arr)-1,-1,-1):
            print("j: "+str(j)) ## DELETEME:
            cur = max(arr[j], greatest)
            print("cur: "+str(cur)) ## DELETEME:
            print("bef arr: "+str(arr)) ## DELETEME:
            arr[j] = greatest
            print("af arr: "+str(arr)) ## DELETEME:
            greatest = cur
        return arr

if __name__ == "__main__":
    solution = Solution()

# Test Case 1
    arr1 = [17, 18, 5, 4, 6, 1]
    output1 = solution.replaceElements(arr1)
    print("Test Case 1:", output1)
# Expected output: [18, 6, 6, 6, 1, -1]

# Test Case 2
    arr2 = [400]
    output2 = solution.replaceElements(arr2)
    print("Test Case 2:", output2)
# Expected output: [-1]

