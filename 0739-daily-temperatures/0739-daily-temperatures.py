class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output: List = [ 0 for idx in temperatures ]
        stack: List = [] # (temp,index)

        for (idx,temper) in enumerate(temperatures):
            while (len(stack) > 0) and (temper > stack[-1][0]):
                (_, stack_idx) = stack.pop()
                dist = idx - stack_idx
                output[stack_idx] = dist

            stack.append((temper, idx))

        return output
