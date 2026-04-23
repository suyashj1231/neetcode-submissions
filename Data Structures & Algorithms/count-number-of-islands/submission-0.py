class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        island_count = 0
        neighbour = [(1,0), (0,1), (0,-1), (-1,0)]

        def dfs(r,c):          
            if (min(r,c) < 0 or
               r >= ROWS or c >= COLS or
               grid[r][c] == '0') :
                return
            
            grid[r][c] = '0'

            for dr,dc in neighbour:
                dfs(r+dr,c+dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    island_count +=1
                    dfs(r,c)
        
        return island_count
            


