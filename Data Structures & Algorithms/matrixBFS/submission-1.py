from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        queue = deque()
        length = 0
        queue.append((0,0))
        visited.add((0,0))
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                if row == ROWS - 1 and col == COLS - 1:
                    return length

                neighbour = [[1,0], [0,1], [-1,0], [0,-1]]

                for dr, dc in neighbour:
                    nrow = row + dr
                    ncol = col + dc

                    if (min(nrow, ncol) < 0 or
                    nrow >= ROWS or ncol >= COLS or
                    grid[nrow][ncol] == 1 or
                    (nrow, ncol) in visited):
                        continue
                    
                    visited.add((nrow, ncol))
                    queue.append((nrow, ncol))
                
            length +=1
        
        return -1
        



