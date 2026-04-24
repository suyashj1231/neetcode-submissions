from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
        

        while queue:
            row, col = queue.popleft()
            for dr, dc in neighbours:
                newr = row + dr
                newc = col + dc

                if (min(newr, newc) < 0 or
                newr >= ROWS or newc >= COLS or
                grid[newr][newc] == 0 or 
                grid[newr][newc] == -1):
                    continue
                
                if grid[newr][newc] == 2147483647:
                    grid[newr][newc] = grid[row][col] + 1
                    queue.append((newr, newc))






        
        
        