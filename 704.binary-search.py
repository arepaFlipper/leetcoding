from typing import List

# @leet start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        (left, right) = (0, len(nums))

        while left <= right:
            mid = (left + right) //2
            current = nums[mid]

            if current == target:
                return mid

            if target < current:
                right = mid - 1

            if current < target:
                left = mid +1

        return -1
        
                
        
# @leet end

# Test functions
def test_binary_search_case_0():
    solution = Solution()
    nums = [1,3,3,4,5,6,7,8]
    target = 8
    expected = 7
    result = solution.search(nums, target)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 1 succeed 👍")

def test_binary_search_case_1():
    solution = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    expected = 4
    result = solution.search(nums, target)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 1 succeed 👍")

def test_binary_search_case_2():
    solution = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    expected = -1
    result = solution.search(nums, target)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 2 succeed 👍")

def test_binary_search_case_3():
    solution = Solution()
    nums = [5]
    target = 5
    expected = 0
    result = solution.search(nums, target)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 3 succeed 👍")

def test_binary_search_case_4():
    solution = Solution()
    nums = [2, 5]
    target = 5
    expected = 1
    result = solution.search(nums, target)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 4 succeed 👍")

def test_binary_search_case_5():
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 6
    expected = 5
    result = solution.search(nums, target)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 5 succeed 👍")

def main():
    # Simulate running tests
    test_binary_search_case_0()
    test_binary_search_case_1()
    test_binary_search_case_2()
    test_binary_search_case_3()

if __name__ == "__main__":
    main()
