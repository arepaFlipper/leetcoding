from typing import List
# @leet start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return quickSort(nums, 0, len(nums) - 1)


# Implementation of QuickSort
def quickSort(arr: list[int], s: int, e: int) -> list[int]:
  if e - s + 1 <= 1:
    return arr

  pivot = arr[e]
  left = s # pointer for left side

  # Partition: elements smaller than pivot on left side
  for i in range(s, e):
    if arr[i] < pivot:
      tmp = arr[left]
      arr[left] = arr[i]
      arr[i] = tmp
      left += 1
      print("""🔍   \x1b[1;33;40m912.sort-an-array.py:23  arr:""") ## DELETEME:
      print(arr) ## DELETEME:
      print('\x1b[0m') ## DELETEME:

  # move pivot in-between left & right sides
  arr[e] = arr[left]
  arr[left] = pivot

  print("""🏞️   \x1b[1;34;40m912.sort-an-array.py:27  arr:""") ## DELETEME:
  print(arr) ## DELETEME:
  print('\x1b[0m') ## DELETEME:
  # Quick sort left side
  quickSort(arr, s, left - 1)

  # Quick sort right side
  quickSort(arr, left + 1, e)

  return arr

        
# @leet end

def test_sort_array_case_0():
    solution = Solution()
    nums = [6,2,4,1,3]
    expected_output = [1,2,3,4,6]
    result = solution.sortArray(nums)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 1 passed")

def test_sort_array_case_1():
    solution = Solution()
    nums = [2,3,4,1,6]
    expected_output = [1,2,3,4,6]
    result = solution.sortArray(nums)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 1 passed")

# Test Cases
def test_sort_array_case_2():
    solution = Solution()
    nums = [5, 2, 3, 1]
    expected_output = [1, 2, 3, 5]
    result = solution.sortArray(nums)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 1 passed")

def test_sort_array_case_3():
    solution = Solution()
    nums = [5, 1, 1, 2, 0, 0]
    expected_output = [0, 0, 1, 1, 2, 5]
    result = solution.sortArray(nums)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 2 passed")

def test_sort_array_case_4():
    solution = Solution()
    nums = [1]
    expected_output = [1]
    result = solution.sortArray(nums)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 3 passed")

def test_sort_array_case_5():
    solution = Solution()
    nums = [-1, -5, -3, 0, 2, 4]
    expected_output = [-5, -3, -1, 0, 2, 4]
    result = solution.sortArray(nums)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 4 passed")

def test_sort_array_case_6():
    solution = Solution()
    nums = [10000, -10000, 0, 9999, -9999]
    expected_output = [-10000, -9999, 0, 9999, 10000]
    result = solution.sortArray(nums)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 5 passed")

def test_sort_array_case_7():
    solution = Solution()
    nums = [3, 3, 3, 3]
    expected_output = [3, 3, 3, 3]
    result = solution.sortArray(nums)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 6 passed")

def test_sort_array_case_8():
    solution = Solution()
    nums = [4, -2, 4, -2, 0]
    expected_output = [-2, -2, 0, 4, 4]
    result = solution.sortArray(nums)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 7 passed")

def test_sort_array_case_9():
    solution = Solution()
    nums = [5 * 10**4, -5 * 10**4, 0, 3, -3]
    expected_output = [-50000, -3, 0, 3, 50000]
    result = solution.sortArray(nums)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 8 passed")

def test_sort_array_case_10():
    solution = Solution()
    nums = [i for i in range(500, -1, -1)]  # Large array sorted in reverse
    expected_output = sorted(nums)  # Expected output: ascending order
    result = solution.sortArray(nums)
    assert result == expected_output, f"Expected {expected_output[:5]}..., but got {result[:5]}..."
    print("Case 9 passed")

def test_sort_array_case_11():
    solution = Solution()
    nums = [i % 7 for i in range(1, 100)]  # Repeated patterns
    expected_output = sorted(nums)
    result = solution.sortArray(nums)
    assert result == expected_output, f"Expected {expected_output[:5]}..., but got {result[:5]}..."
    print("Case 10 passed")

# Main test execution
def main():
    test_sort_array_case_0()
    # test_sort_array_case_1()
    # test_sort_array_case_2()
    # test_sort_array_case_3()
    # test_sort_array_case_4()
    # test_sort_array_case_5()
    # test_sort_array_case_6()
    # test_sort_array_case_7()
    # test_sort_array_case_8()
    # test_sort_array_case_9()
    # test_sort_array_case_10()
    #
if __name__ == "__main__":
    main()

