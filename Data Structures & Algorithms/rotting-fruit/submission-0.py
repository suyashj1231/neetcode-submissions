from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        neighbours = [(1,0), (0,1),(-1,0), (0,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        fresh = 0
        out = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))

                elif grid[r][c] == 1:
                    fresh +=1
                else:
                    continue

        # multi_bfs()
        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in neighbours:
                    newr = row + dr
                    newc = col + dc

                    if (min(newr, newc) < 0 or
                    newr >= ROWS or newc >= COLS or
                    grid[newr][newc] == 2 or 
                    grid[newr][newc] == 0):
                        continue
                    
                    if grid[newr][newc] == 1:
                        fresh -= 1
                        queue.append((newr,newc))
                        grid[newr][newc] = 2
            
            out +=1

        if fresh == 0:
            return out
        else:
            return -1