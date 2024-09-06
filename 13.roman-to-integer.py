class Solution:
    def romanToInt(self, s: str) -> int:
        length = len(s)
        idx = 0
        res = 0
        reversed = s[::-1]
        substraction_cases = ["I","X","C"]
        print("""🌯   \x1b[1;34;40m13.roman-to-integer.py:6 reversed:""") ## DELETEME:
        print(reversed) ## DELETEME:
        print('\x1b[0m') ## DELETEME:
        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        while idx <= length - 1 :
            char = reversed[idx]
            current = hashmap[char]
            idx = idx + 1
            next_char = 0
            next_val = 0
            if idx <length:
                next_char = reversed[idx]
                next_val = hashmap[next_char]
            if next_val < current and next_char in substraction_cases:
                current = current - next_val
                idx = idx + 1
                print("""🍹   \x1b[1;36;40m13.roman-to-integer.py:29    idx:""") ## DELETEME:
                print(idx) ## DELETEME:
                print('\x1b[0m') ## DELETEME:
            res = res + current
            print("""♉   \x1b[1;32;40m13.roman-to-integer.py:30    res:""") ## DELETEME:
            print(res , " idx: " , idx) ## DELETEME:
            print('\x1b[0m') ## DELETEME:
        print("""📰    \x1b[1;33;40m13.roman-to-integer.py:30    res:""") ## DELETEME:
        print(res) ## DELETEME:
        print('\x1b[0m') ## DELETEME:
        return res

# Test functions
def test_roman_to_int_case_1():
    solution = Solution()
    s = "III"
    expected = 3
    result = solution.romanToInt(s)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 1 succeed 👍")

def test_roman_to_int_case_2():
    solution = Solution()
    s = "LVIII"
    expected = 58
    result = solution.romanToInt(s)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 2 succeed 👍")

def test_roman_to_int_case_3():
    solution = Solution()
    s = "MCMXCIV"
    expected = 1994
    result = solution.romanToInt(s)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 3 succeed 👍")

def test_roman_to_int_case_4():
    solution = Solution()
    s = "IX"
    expected = 9
    result = solution.romanToInt(s)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 4 succeed 👍")

def test_roman_to_int_case_5():
    solution = Solution()
    s = "XL"
    expected = 40
    result = solution.romanToInt(s)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 5 succeed 👍")

def main():
    # Simulate running tests
    test_roman_to_int_case_1()
    test_roman_to_int_case_2()
    test_roman_to_int_case_3()
    test_roman_to_int_case_4()
    test_roman_to_int_case_5()

if __name__ == "__main__":
    main()

