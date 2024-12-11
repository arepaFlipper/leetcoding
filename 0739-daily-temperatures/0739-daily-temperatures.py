class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List = [] # (idx,t)
        res: List = [0 for t in (temperatures)]

        for (idx,temp) in enumerate(temperatures):
            while (len(stack)>0 and stack[-1][1] < temp ):
                (stack_idx, _) = stack.pop()
                dist = idx - stack_idx
                res[stack_idx] = dist

            stack.append((idx,temp))
        return res
