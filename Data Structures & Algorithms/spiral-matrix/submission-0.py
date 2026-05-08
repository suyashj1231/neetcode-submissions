class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        seen = set()
        res = []
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows = len(matrix)
        cols = len(matrix[0])

        # start at 0, 0
        r,c = 0, 0 
        di = 0

        while len(res) < rows * cols:
            res.append(matrix[r][c])
            seen.add((r,c))

            dr,dc = direction[di]
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen:
                r, c = nr, nc
            else:
                di = (di + 1) % 4
                dr, dc = direction[di]
                r, c = r + dr, c + dc
        
        return res