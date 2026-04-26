class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i, distance):
            if i >= len(cost):
                return distance

            return min(dfs(i+1, distance+ cost[i]), dfs(i+2, distance+ cost[i]))

        return min(dfs(0,0),dfs(1,0))