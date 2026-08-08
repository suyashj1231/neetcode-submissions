from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbours = [(1,0),(0,1),(-1,0),(0,-1)] # we can move like this dawg
        island = 0
        seen = set()

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            seen.add((r,c))
            while queue:
                r,c = queue.popleft()
                for row, col in neighbours:
                    dr = r + row
                    dc = c + col

                    if (min(dr,dc) < 0 or 
                    dr >= ROWS or dc >= COLS or 
                    grid[dr][dc] == "0" or 
                    (dr, dc) in seen):
                        continue
                    queue.append((dr, dc))
                    seen.add((dr, dc))

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in seen:
                    bfs(r,c)
                    island +=1

        return island
                    

        