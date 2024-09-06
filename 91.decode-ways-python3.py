class Solution:
    def numDecodings(self, s: str) -> int:
        n: int = len(s)

        # NOTE: Initialize a dictionary to store the number of ways to decode the string from
        # index `i` onward.
        # The base case is when `i=n`, which means we're past the last character,
        # so there is 1 way to decode (an empty string).
        dp: dict = {n:1}

        # NOTE: Iterate over the string in reverse order, starting from the last character back to the first.
        # This allows us to build up the colution by considering all possible substrings.
        for idx in range(n-1, -1, -1):
            # NOTE: If the current character is '0', it cannot form a valid decoding by itself.
            # Hence, the number of ways to decode from this index is 0.
            if s[idx] == "0":
                dp[idx] = 0
            else:
                # NOTE:  If the current character is different than '0', the number of ways to decode
                # from this index is at least the number of ways to decode from the next index.
                dp[idx] = dp[idx + 1]


            # NOTE: Check if the current and the next character together can form a valid
            # two-digit number (10 to 26). 
            # This is possible if the current character is '1', or if it is '2' 
            # and the next character is between '0' and '6'.
            if idx + 1 < n and (s[idx] == "1" or s[idx]=="2" and s[idx +1] in "0123456"):
                # NOTE:  If the two-digit number is valid, add the number of ways to decode from the index
                # after the next one. This accounts for the cae where we use both characters together as 
                # one decoding step.
                dp[idx] += dp[idx +2]

        # NOTE: The total of ways to decode is accumulated in the '0' key.
        return dp[0]

solution = Solution()

# Test Case 1
input_str_1 = "12"
expected_output_1 = 2
print("Test Case 1:")
result_1 = solution.numDecodings(input_str_1)

print("Input:")
print("s:", input_str_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output\nExpected:", expected_output_1)

# Test Case 2
input_str_2 = "226"
expected_output_2 = 3
print("\nTest Case 2:")
result_2 = solution.numDecodings(input_str_2)

print("Input:")
print("s:", input_str_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output\nExpected:", expected_output_2)

# Test Case 3
input_str_3 = "06"
expected_output_3 = 0
print("\nTest Case 3:")
result_3 = solution.numDecodings(input_str_3)

print("Input:")
print("s:", input_str_3)
print("Output:", result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output\nExpected:", expected_output_3)

# Test Case 4
input_str_4 = "11106"
expected_output_4 = 2
print("Test Case 4:")
result_4 = solution.numDecodings(input_str_4)

print("Input:")
print("s:", input_str_4)
print("Output:", result_4)

if result_4 == expected_output_4:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output\nExpected:", expected_output_4)


# Test Case 4
input_str_5 = "27"
expected_output_5 = 1
print("Test Case 5:")
result_5 = solution.numDecodings(input_str_5)

print("Input:")
print("s:", input_str_5)
print("Output:", result_5)

if result_5 == expected_output_5:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output\nExpected:", expected_output_5)
