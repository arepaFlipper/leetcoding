class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        prev_min = val
        if len(self.minStack) > 0:
            prev_min = self.minStack[-1]
        
        self.minStack.append(min(val,prev_min))
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Test Case 1
minStack1 = MinStack()
minStack1.push(3)
minStack1.push(1)
minStack1.push(5)
minStack1.push(2)

print("Test Case 1 - getMin:", minStack1.getMin())  # Expected output: 1
print("Test Case 1 - top:", minStack1.top())  # Expected output: 2

minStack1.pop()
print("Test Case 1 - getMin after pop:", minStack1.getMin())  # Expected output: 1
print("Test Case 1 - top after pop:", minStack1.top())  # Expected output: 5

# Test Case 2
minStack2 = MinStack()
minStack2.push(4)
minStack2.push(2)
minStack2.push(6)

print("Test Case 2 - getMin:", minStack2.getMin())  # Expected output: 2
print("Test Case 2 - top:", minStack2.top())  # Expected output: 6

minStack2.pop()
print("Test Case 2 - getMin after pop:", minStack2.getMin())  # Expected output: 2
print("Test Case 2 - top after pop:", minStack2.top())  # Expected output: 2
