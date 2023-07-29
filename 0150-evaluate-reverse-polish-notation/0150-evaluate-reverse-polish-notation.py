class Solution:
    def operate (self,v1,op,v2):
        res = 0
        if op == '+':
            res = v1 + v2
        if op == '-':
            res = v1 - v2
        if op == '*':
            res = v1 * v2
        if op == '/':
            res = int(v1 / v2)
        
        return res

    def evalRPN(self, tokens: list[str]) -> int:
        stack: list = []
        arith_op: list = ['+','-','/','*']

        for (idx,val) in enumerate(tokens):

            if val not in arith_op:
                res = int(val)
                stack.append(res)
            elif val in arith_op:
                v2= int(stack[-1])
                stack.pop()
                v1= int(stack[-1])
                stack.pop()
                res = self.operate(v1,val,v2)
                stack.append(res)
        return stack[0]

    def test_evalRPN(self):
        # Test Case 1
        tokens1 = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
        print("Test Case 1:", self.evalRPN(tokens1))  # Expected output: 893

        # Test Case 2
        tokens2 = ["2","1","+","3","*"]
        print("Test Case 2:", self.evalRPN(tokens2))  # Expected output: 9

        # Test Case 3
        tokens3 = ["4","13","5","/","+"]
        print("Test Case 3:", self.evalRPN(tokens3))  # Expected output: 6

        # Test Case 4
        tokens4 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        print("Test Case 4:", self.evalRPN(tokens4))  # Expected output: 22

        # Test Case 5
        tokens5 = ["18"]
        print("Test Case 5:", self.evalRPN(tokens5))  # Expected output: 18


# Create an instance of the Solution class and run the tests
solution = Solution()
solution.test_evalRPN()




