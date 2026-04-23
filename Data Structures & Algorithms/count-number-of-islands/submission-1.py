from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        island_count = 0
        neighbour = [(1,0), (0,1), (0,-1), (-1,0)]
        seen = set()       
        
        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            seen.add((r,c))

            while queue:
                row,col = queue.popleft()

                for (dr, dc) in neighbour:
                    new_r = row + dr
                    new_c = col + dc

                    if (min(new_r, new_c) < 0 or
                    new_r >= ROWS or new_c >= COLS or
                    (new_r, new_c) in seen or
                    grid[new_r][new_c] == '0'):
                        continue
                    
                    queue.append((new_r, new_c))
                    seen.add((new_r, new_c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in seen:
                    bfs(r,c)
                    island_count +=1

        return island_count








        # def dfs(r,c):          
        #     if (min(r,c) < 0 or
        #        r >= ROWS or c >= COLS or
        #        grid[r][c] == '0') :
        #         return
            
        #     grid[r][c] = '0'
        #     for dr,dc in neighbour:
        #         dfs(r+dr,c+dc)
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == '1':
        #             island_count +=1
        #             dfs(r,c)
        
        # return island_count
            


