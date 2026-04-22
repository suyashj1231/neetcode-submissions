class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # no 2 queen in same row / column and along diagonal of 1 another
        cols = set()
        pos_dia = set()
        neg_dia = set()
        res = []

        board = [['.']* n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy_board = ["".join(row) for row in board]
                res.append(copy_board)
                return
            
            for c in range(n):
                if (c in cols or
                (r+c) in pos_dia or
                (r-c) in neg_dia):
                    continue

                pos_dia.add(r+c)
                neg_dia.add(r-c)
                cols.add(c)
                board[r][c] = "Q"

                backtrack(r+1)

                pos_dia.remove(r+c)
                neg_dia.remove(r-c)
                cols.remove(c)
                board[r][c] = "."
        
        backtrack(0)
        return res


