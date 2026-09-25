class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def memoization(i, buffer):
            if (i, buffer) in memo:
                return memo[(i, buffer)]
            if i == len(days):
                return 0
            day = days[i]
            if day <= buffer:
                memo[(i, buffer)] = memoization(i+1, buffer)
            else:
                memo[(i, buffer)] = min(costs[0] + memoization(i+1, day),
                costs[1]+ memoization(i+1, day+6),
                costs[2] + memoization(i+1, day+29))
            
            return memo[(i, buffer)]
    
        return memoization(0,0)


