class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}

        def dfs(i, buffer):
            if i == len(days):
                return 0
            if (i, buffer) in memo:
                return memo[(i, buffer)]

            day = days[i]
            if day <= buffer:
                res = dfs(i + 1, buffer)
            else:
                res = min(
                    costs[0] + dfs(i + 1, day),
                    costs[1] + dfs(i + 1, day + 6),
                    costs[2] + dfs(i + 1, day + 29),
                )

            memo[(i, buffer)] = res
            return res

        return dfs(0, 0)
