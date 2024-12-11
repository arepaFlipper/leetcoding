from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        left = 0
        right = len(A) - 1

        while True:
            adx  = (left + right) // 2 # A
            bdx  = half - adx - 2

            Aleft = A[adx] if adx>= 0 else float ("-infinity")
            Aright = A[adx + 1] if (adx + 1) < len(A) else float("infinity")

            Bleft = B[bdx] if bdx >= 0 else float("-infinity")
            Bright = B[bdx + 1] if (bdx + 1) < len(B) else float("infinity")

            # partition is correct
            if (Aleft <= Bright) and (Bleft <= Aright):
                # odd

                if (total % 2):
                    return min(Aright, Bright)
                # even

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                right = adx - 1
            else:
                left = adx + 1

def test_median_sorted_arrays(nums1, nums2, expected):
    solution = Solution()
    result = solution.findMedianSortedArrays(nums1, nums2)

    print("Input nums1:", nums1)
    print("Input nums2:", nums2)
    print("Output:", result)
    print("Expected:", expected)

    if abs(result - expected) < 1e-5:
        print("✅ Test passed")
    else:
        print("❌ Test failed")

# Test cases
test_median_sorted_arrays([1, 3], [2], 2)
test_median_sorted_arrays([1, 2], [3, 4], 2.5)
test_median_sorted_arrays([1, 3, 8], [2, 7, 10], 5.0)
test_median_sorted_arrays([1, 3, 8], [2, 7], 3)

