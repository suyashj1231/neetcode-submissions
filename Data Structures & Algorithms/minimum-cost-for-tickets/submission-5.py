from functools import lru_cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            if i == len(days):
                return 0
            res = float('inf')
            
            for d, c in zip([1,7,30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j+=1
                res = min(res, dfs(j)+c)
            return res

        return dfs(0)