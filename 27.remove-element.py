from typing import List
# @leet start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(left, len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left
        
# @leet end

# Test functions
def test_remove_element_case_1():
    solution = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    expected_k = 2
    expected_nums = [2, 2]
    k = solution.removeElement(nums, val)
    assert k == expected_k, f"Expected k={expected_k}, but got k={k}"
    assert sorted(nums[:k]) == sorted(expected_nums), f"Expected nums[:k]={expected_nums}, but got nums[:k]={nums[:k]}"
    print("Case 1 passed ✅")

def test_remove_element_case_2():
    solution = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    expected_k = 5
    expected_nums = [0, 1, 3, 0, 4]
    k = solution.removeElement(nums, val)
    assert k == expected_k, f"Expected k={expected_k}, but got k={k}"
    assert sorted(nums[:k]) == sorted(expected_nums), f"Expected nums[:k]={expected_nums}, but got nums[:k]={nums[:k]}"
    print("Case 2 passed ✅")

def test_remove_element_case_3():
    solution = Solution()
    nums = []
    val = 0
    expected_k = 0
    expected_nums = []
    k = solution.removeElement(nums, val)
    assert k == expected_k, f"Expected k={expected_k}, but got k={k}"
    assert nums[:k] == expected_nums, f"Expected nums[:k]={expected_nums}, but got nums[:k]={nums[:k]}"
    print("Case 3 passed ✅")

def test_remove_element_case_4():
    solution = Solution()
    nums = [4, 4, 4]
    val = 4
    expected_k = 0
    expected_nums = []
    k = solution.removeElement(nums, val)
    assert k == expected_k, f"Expected k={expected_k}, but got k={k}"
    assert nums[:k] == expected_nums, f"Expected nums[:k]={expected_nums}, but got nums[:k]={nums[:k]}"
    print("Case 4 passed ✅")

def test_remove_element_case_5():
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    val = 6
    expected_k = 5
    expected_nums = [1, 2, 3, 4, 5]
    k = solution.removeElement(nums, val)
    assert k == expected_k, f"Expected k={expected_k}, but got k={k}"
    assert sorted(nums[:k]) == sorted(expected_nums), f"Expected nums[:k]={expected_nums}, but got nums[:k]={nums[:k]}"
    print("Case 5 passed ✅")

def main():
    # Run test cases
    test_remove_element_case_1()
    test_remove_element_case_2()
    test_remove_element_case_3()
    test_remove_element_case_4()
    test_remove_element_case_5()

if __name__ == "__main__":
    main()
