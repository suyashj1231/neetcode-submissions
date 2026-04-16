class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack 
        res = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stacktemp ,stackindex = stack.pop()
                res[stackindex] = index - stackindex
            stack.append([temp, index])

        return res
        

        