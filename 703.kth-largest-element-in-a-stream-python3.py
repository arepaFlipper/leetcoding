from typing import List

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val: int) -> None:
        print(f"\nPushing {val}")
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self) -> int:
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        print(f"\nPopping {self.heap[0]}")
        self._swap(0, len(self.heap) - 1)
        val = self.heap.pop()
        if self.heap:  # Only bubble down if heap is not empty
            self._bubble_down(0)
            self.print_heap()
        return val

    def peek(self) -> int:
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def _bubble_up(self, index: int) -> None:
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            self._bubble_up(parent)

    def _bubble_down(self, index: int) -> None:
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._bubble_down(smallest)

    def _swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __len__(self) -> int:
        return len(self.heap)

    def print_heap(self) -> None:
        """
        Prints the heap in a tree-like structure.
        """
        if not self.heap:
            print("Heap is empty")
            return

        print(f"Heap array: {self.heap}")
        
        levels = self._calculate_levels()
        height = len(levels)
        
        for i, level in enumerate(levels):
            # Calculate indentation
            indent = " " * (2 ** (height - i - 1))
            # Calculate spacing between nodes at this level
            spacing = " " * (2 ** (height - i) - 1)
            
            # Print nodes with proper alignment
            print(indent + spacing.join(str(x) for x in level))
            
            # Print connections if not last level
            if i < len(levels) - 1:
                next_level = levels[i + 1]
                connections = []
                for j in range(len(level)):
                    left_child_idx = j * 2
                    right_child_idx = j * 2 + 1
                    
                    if left_child_idx < len(next_level):
                        connections.append("/")
                    else:
                        connections.append(" ")
                    
                    if right_child_idx < len(next_level):
                        connections.append(" \\")
                    else:
                        connections.append(" ")
                    
                    if j < len(level) - 1:
                        connections.append(" " * (len(spacing) - 1))
                
                connection_indent = " " * (2 ** (height - i - 1) - 1)
                print(connection_indent + "".join(connections))


    def _calculate_levels(self) -> List[List[int]]:
        """
        Helper function to calculate the nodes at each level of the heap.
        """
        levels = []
        level = 0
        while 2 ** level - 1 < len(self.heap):
            start = 2 ** level - 1
            end = min(2 ** (level + 1) - 1, len(self.heap))
            levels.append(self.heap[start:end])
            level += 1
        return levels


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        print(f"\nInitializing KthLargest with k={k} and nums={nums}")
        self.min_heap = MinHeap()
        self.k = k
        print("\nBuilding initial heap:")
        for num in nums:
            self.min_heap.push(num)
        print("\nRemoving elements until we have k largest:")
        while len(self.min_heap) > k:
            self.min_heap.pop()
        print("\nFinal heap after initialization:")
        self.min_heap.print_heap()

    def add(self, val: int) -> int:
        print(f"\nAdding {val}")
        self.min_heap.push(val)
        if len(self.min_heap) > self.k:
            print(f"\nRemoving smallest element to maintain {self.k} elements:")
            self.min_heap.pop()
        result = self.min_heap.peek()
        print(f"\nCurrent heap after adding {val}:")
        self.min_heap.print_heap()
        print(f"Kth largest element: {result}")
        return result


def test_kth_largest():
    test_cases = [
        {
            "operations": ["KthLargest", "add", "add", "add", "add", "add"],
            "arguments": [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
            "expected": [None, 4, 5, 5, 8, 8],
        },
        # {
        #     "operations": ["KthLargest", "add", "add", "add", "add"],
        #     "arguments": [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]],
        #     "expected": [None, 7, 7, 7, 8],
        # },
        # {
        #     "operations": ["KthLargest", "add", "add", "add"],
        #     "arguments": [[1, []], [5], [10], [9]],
        #     "expected": [None, 5, 10, 10],
        # },
        # {
        #     "operations": ["KthLargest", "add", "add", "add", "add", "add"],
        #     "arguments": [[2, [1, 2]], [3], [4], [5], [6], [7]],
        #     "expected": [None, 2, 3, 4, 5, 6],
        # },
        # {
        #     "operations": ["KthLargest", "add", "add", "add", "add", "add"],
        #     "arguments": [[3, [10, 9, 8]], [7], [6], [5], [11], [12]],
        #     "expected": [None, 8, 8, 8, 9, 10],
        # },
    ]

    for i, test in enumerate(test_cases):
        obj = None
        result = []

        try:
            for op, args in zip(test["operations"], test["arguments"]):
                if op == "KthLargest":
                    obj = KthLargest(*args)
                    result.append(None)
                elif op == "add":
                    result.append(obj.add(*args))
                    print(f"After adding {args[0]}, the heap is:")
                    obj.min_heap.print_heap()  # Changed from obj.print_heap() to obj.min_heap.print_heap()
                print("-" * 40)

            assert result == test["expected"], f"Test {i + 1} failed: Expected {test['expected']}, got {result}"
            print(f"Test {i + 1} passed! ✅")
        except Exception as e:
            print(f"Test {i + 1} failed with error: {e} ❌")


# Run tests
if __name__ == "__main__":
    test_kth_largest()
