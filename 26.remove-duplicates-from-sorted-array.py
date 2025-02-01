from typing import List
# @leet start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(left, len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1
        return left
        
# @leet end
# Solution class

# Test functions
def test_remove_duplicates_case_1():
    solution = Solution()
    nums = [1, 1, 2]
    expected_k = 2
    expected_nums = [1, 2]
    k = solution.removeDuplicates(nums)
    assert k == expected_k, f"Expected k={expected_k}, but got k={k}"
    assert nums[:k] == expected_nums, f"Expected nums[:k]={expected_nums}, but got nums[:k]={nums[:k]}"
    print("Case 1 passed ✅")

def test_remove_duplicates_case_2():
    solution = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_k = 5
    expected_nums = [0, 1, 2, 3, 4]
    k = solution.removeDuplicates(nums)
    assert k == expected_k, f"Expected k={expected_k}, but got k={k}"
    assert nums[:k] == expected_nums, f"Expected nums[:k]={expected_nums}, but got nums[:k]={nums[:k]}"
    print("Case 2 passed ✅")

def test_remove_duplicates_case_3():
    solution = Solution()
    nums = [1]
    expected_k = 1
    expected_nums = [1]
    k = solution.removeDuplicates(nums)
    assert k == expected_k, f"Expected k={expected_k}, but got k={k}"
    assert nums[:k] == expected_nums, f"Expected nums[:k]={expected_nums}, but got nums[:k]={nums[:k]}"
    print("Case 3 passed ✅")

def test_remove_duplicates_case_4():
    solution = Solution()
    nums = [1, 1, 1, 1]
    expected_k = 1
    expected_nums = [1]
    k = solution.removeDuplicates(nums)
    assert k == expected_k, f"Expected k={expected_k}, but got k={k}"
    assert nums[:k] == expected_nums, f"Expected nums[:k]={expected_nums}, but got nums[:k]={nums[:k]}"
    print("Case 4 passed ✅")

def test_remove_duplicates_case_5():
    solution = Solution()
    nums = [-1, 0, 0, 0, 3, 3, 3, 4, 5]
    expected_k = 5
    expected_nums = [-1, 0, 3, 4, 5]
    k = solution.removeDuplicates(nums)
    assert k == expected_k, f"Expected k={expected_k}, but got k={k}"
    assert nums[:k] == expected_nums, f"Expected nums[:k]={expected_nums}, but got nums[:k]={nums[:k]}"
    print("Case 5 passed ✅")

def main():
    # Run test cases
    test_remove_duplicates_case_1()
    test_remove_duplicates_case_2()
    test_remove_duplicates_case_3()
    test_remove_duplicates_case_4()
    test_remove_duplicates_case_5()

if __name__ == "__main__":
    main()

