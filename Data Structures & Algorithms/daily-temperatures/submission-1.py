class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack 
        res = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackindex, stacktemp = stack.pop()
                res[stackindex] = index - stackindex
            stack.append([index, temp])

        return res
        

        