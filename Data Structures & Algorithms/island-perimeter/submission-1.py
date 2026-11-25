class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        neighbours = [(0,1), (1,0), (-1,0), (0,-1)]
        queue = deque()
        peri = 0
        visited = set()

        for i in range(len(grid)):
            found = False
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    found = True
                    break
            if found:
                break

        while queue:
            row,col = queue.popleft()
            if (row,col) in visited: continue
            visited.add((row,col))
            cnt = 4
            for r, c in neighbours:
                nr = row + r
                nc = col + c

                if (min(nr,nc) >= 0 and
                nr < len(grid) and nc< len(grid[0]) and
                grid[nr][nc] == 1):
                    cnt -= 1
                    if (nr,nc) not in visited:
                        queue.append((nr,nc))
            peri += cnt

        return peri