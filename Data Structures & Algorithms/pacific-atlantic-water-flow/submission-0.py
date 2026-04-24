class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        neighbours = [(1,0), (0,1),(-1,0), (0,-1)]
        ROWS = len(heights)
        COLS = len(heights[0])

        
        def dfs(row, col, visit, prevheight):
            if (min(row,col) < 0 or
            row >= ROWS or col >= COLS or
            heights[row][col] < prevheight or 
            (row,col) in visit):
                return
                
            visit.add((row,col))
            for dr, dc in neighbours:
                r = row + dr
                c = col + dc
                
                dfs(r, c, visit, heights[row][col])

            # For Pacific (Top and Left)
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])

        # For Atlantic (Bottom and Right)
        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        res = pacific.intersection(atlantic)

        return [[r, c] for r, c in res]