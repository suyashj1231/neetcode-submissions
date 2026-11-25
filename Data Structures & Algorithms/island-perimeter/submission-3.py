class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res += 4
                    if r and grid[r-1][c]: res -= 2
                    if c and grid[r][c-1]: res -= 2
        return res