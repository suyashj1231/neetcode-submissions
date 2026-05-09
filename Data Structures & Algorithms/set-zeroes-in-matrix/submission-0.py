class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        zeros = set()
        # Find all zeros
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zeros.add((r, c))
        
        # Set rows and columns to zero
        for r, c in zeros:
            for col in range(COLS):
                matrix[r][col] = 0
            for row in range(ROWS):
                matrix[row][c] = 0
 
        