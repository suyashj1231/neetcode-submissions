from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbours = [(1,0),(0,1),(-1,0),(0,-1)] # we can move like this dawg
        island = 0

        def dfs(i,j):
            if (i < 0 or j < 0 or
            i >= ROWS or j >= COLS or
            grid[i][j] == '0'):
                return
            grid[i][j] = '0'
            for r,c in neighbours:
                dr = i + r
                dc = j + c
                dfs(dr,dc)
            
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    island +=1
                    
                    dfs(i,j)

        return island
            
            

            
            
            
           
            
