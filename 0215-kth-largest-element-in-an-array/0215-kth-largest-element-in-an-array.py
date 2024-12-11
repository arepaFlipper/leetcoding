from typing import List
class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[right]
        fill = left

        for i in range(left,right):
            if nums[i] <= pivot:
                (nums[fill],nums[i]) = (nums[i], nums[fill] )
                fill +=1
        (nums[fill], nums[right]) = (nums[right], nums[fill])
        return fill

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left = 0
        right = len(nums)-1

        while left < right:
            pivot = self.partition(nums,left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]

solution = Solution()

# Test Case 1
input_nums_1 = [3, 2, 1, 5, 6, 4]
input_k_1 = 2
expected_output_1 = 5
result_1 = solution.findKthLargest(input_nums_1, input_k_1)

print("Test Case 1:")
print("Input:")
print("nums:", input_nums_1)
print("k:", input_k_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_nums_2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
input_k_2 = 4
expected_output_2 = 4
result_2 = solution.findKthLargest(input_nums_2, input_k_2)

print("\nTest Case 2:")
print("Input:")
print("nums:", input_nums_2)
print("k:", input_k_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
