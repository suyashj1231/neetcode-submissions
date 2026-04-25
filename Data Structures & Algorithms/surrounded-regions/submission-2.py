class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        neighbours = [(1,0), (0,1), (-1,0), (0,-1)]
        # find all the border adj "O"
        def dfs(r,c):
            if (min(r,c) < 0 or
            r >= ROWS or c >= COLS or 
            board[r][c] != 'O') or (r,c) in visited:
                return
            
            if board[r][c] == "O":
                visited.add((r,c))
                for i, j in neighbours:
                    dr, dc = r +i, c + j
                    dfs(dr, dc)
        
        # 1. dfs on border

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        # 2. change all O not in visited to X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"
        


