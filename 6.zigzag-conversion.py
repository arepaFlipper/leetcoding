# @leet start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        total = len(s)
        if numRows == 1:
            return s
        increment = (numRows-1) * 2
        res = ""
        for row in range(numRows):
            for idx in range(row, total, increment):
                res += s[idx]
                extra_char_idx = idx +  increment - (2*row)
                if( row > 0 and row < (numRows - 1) and extra_char_idx < total):
                    res += s[extra_char_idx]
            
        return res

        
# @leet end

# Solution class
# Test functions

def test_zigzag_conversion_case_1():
    solution = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    expected = "PAHNAPLSIIGYIR"
    result = solution.convert(s, numRows)
    if result == expected:
        print("Case 1 passed ✅")
    else:
        print(f"Expected {expected}, but got {result} ❌ ")


def test_zigzag_conversion_case_2():
    solution = Solution()
    s = "PAYPALISHIRING"
    numRows = 4
    expected = "PINALSIGYAHRPI"
    result = solution.convert(s, numRows)
    if result == expected:
        print("Case 2 passed ✅")
    else:
        print(f"Expected {expected}, but got {result} ❌ ")

def test_zigzag_conversion_case_3():
    solution = Solution()
    s = "A"
    numRows = 1
    expected = "A"
    result = solution.convert(s, numRows)
    if result == expected:
        print("Case 2 passed ✅")
    else:
        print(f"Expected {expected}, but got {result} ❌ ")

def test_zigzag_conversion_case_4():
    solution = Solution()
    s = "AB"
    numRows = 1
    expected = "AB"
    result = solution.convert(s, numRows)
    if result == expected:
        print("Case 4 passed ✅")
    else:
        print(f"Expected {expected}, but got {result} ❌ ")

def test_zigzag_conversion_case_5():
    solution = Solution()
    s = "ABCDEFGH"
    numRows = 2
    expected = "ACEGBDFH"
    result = solution.convert(s, numRows)
    if result == expected:
        print("Case 5 passed ✅")
    else:
        print(f"Expected {expected}, but got {result} ❌ ")

def test_zigzag_conversion_case_6():
    solution = Solution()
    s = "HELLOWORLD"
    numRows = 5
    expected = "HLERDLOLWO"
    result = solution.convert(s, numRows)
    if result == expected:
        print("Case 5 passed ✅")
    else:
        print(f"Expected {expected}, but got {result} ❌ ")

def main():
    # Run test cases
    test_zigzag_conversion_case_1()
    test_zigzag_conversion_case_2()
    test_zigzag_conversion_case_3()
    test_zigzag_conversion_case_4()
    test_zigzag_conversion_case_5()
    test_zigzag_conversion_case_6()

if __name__ == "__main__":
    main()

