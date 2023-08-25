class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack: List = []
        for val in (operations):
            print("val:",val) ## DELETEME:
            if val == "+":
                sum = stack[-1] + stack[-2]
                stack.append(sum)

            elif val == "D":
                doubled = 2*stack[-1]
                stack.append(doubled)

            elif val == "C":
                stack.pop()

            elif "-" in val:
                v = val[1:]
                v = int(v)
                v = v * (-1)
                stack.append(v)

            elif val.isdigit():
                stack.append(int(val))

            print(stack) ## DELETEME:

        res = 0
        print("final stack:",stack) ## DELETEME:
        for v in stack:
            res += v
        return res

