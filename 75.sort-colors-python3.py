class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        bucket = len(hashmap.keys()) * [0]
        # Assuming three colors: 0, 1, 2
        # bucket = 3 * [0]
        for num in nums:
            bucket[num] += 1

        idx = 0
        for color in range(3):
            for _ in range(bucket[color]):
                nums[idx] = color
                idx += 1
        return nums

        
def test_sort_array_case_0():
    solution = Solution()
    nums = [2,0,2,1,1,0]
    expected_output = [0,0,1,1,2,2]
    result = solution.sortColors(nums)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 1 passed")

# Main test execution
def main():
    test_sort_array_case_0()
    #

if __name__ == "__main__":
    main()

