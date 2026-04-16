class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        top_row = 0
        bottom_row = rows - 1

        while top_row <= bottom_row:
            curr_row = (top_row + bottom_row) // 2

            if target > matrix[curr_row][-1]:
                top_row = curr_row + 1
            
            elif target < matrix[curr_row][0]:
                bottom_row = curr_row - 1
            
            else:
                break
        
        if not (top_row <= bottom_row):
            return False
        
        curr_row = (top_row + bottom_row) // 2
        l = 0
        r = cols - 1
        while l <=r:
            m = l + (r-l) // 2

            if target > matrix[curr_row][m]:
                l = m+ 1
            elif target < matrix[curr_row][m]:
                r = m - 1
            else:
                return True
        return False 

