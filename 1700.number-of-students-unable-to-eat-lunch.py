# Solution class
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        left = 0
        reversed_students = students[::-1]
        reversed_sandwiches = sandwiches[::-1]
        while (left < len(reversed_students)):
            if reversed_students[-1] == reversed_sandwiches[-1]:
                reversed_sandwiches.pop()
                reversed_students.pop()
                left = 0
            else:
                frustrated_kido = reversed_students.pop()
                reversed_students = reversed_students[::-1]
                reversed_students.append(frustrated_kido)
                reversed_students = reversed_students[::-1]
                left += 1
            print("""🎄   \x1b[1;34;40m1700.number-of-students-unable-to-eat-lunch.py:16    reversed_sandwiches:""") ## DELETEME:
            print("reversed_students:   ",reversed_students, "\nreversed_sandwiches: ", reversed_sandwiches) ## DELETEME:
            print('\x1b[0m') ## DELETEME:
        return left
                

# Test functions
def test_count_students_case_1():
    solution = Solution()
    students = [1, 1, 0, 0]
    sandwiches = [0, 1, 0, 1]
    expected_output = 0
    result = solution.countStudents(students, sandwiches)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 1 passed")

def test_count_students_case_2():
    solution = Solution()
    students = [1, 1, 1, 0, 0, 1]
    sandwiches = [1, 0, 0, 0, 1, 1]
    expected_output = 3
    result = solution.countStudents(students, sandwiches)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 2 passed")

def test_count_students_case_3():
    solution = Solution()
    students = [0, 0, 0]
    sandwiches = [1, 1, 1]
    expected_output = 3
    result = solution.countStudents(students, sandwiches)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 3 passed")

def test_count_students_case_4():
    solution = Solution()
    students = [1, 0, 1, 0]
    sandwiches = [0, 0, 1, 1]
    expected_output = 0
    result = solution.countStudents(students, sandwiches)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 4 passed")

def test_count_students_case_5():
    solution = Solution()
    students = [0, 1, 0, 1, 1]
    sandwiches = [1, 0, 1, 1, 0]
    expected_output = 1
    result = solution.countStudents(students, sandwiches)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 5 passed")

def test_count_students_case_6():
    solution = Solution()
    students = [0, 0, 0, 1, 1, 1]
    sandwiches = [0, 0, 0, 1, 1, 1]
    expected_output = 0
    result = solution.countStudents(students, sandwiches)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Case 6 passed")

def main():
    # Run test cases
    test_count_students_case_1()
    test_count_students_case_2()
    test_count_students_case_3()
    test_count_students_case_4()
    # test_count_students_case_5()
    test_count_students_case_6()

if __name__ == "__main__":
    main()

