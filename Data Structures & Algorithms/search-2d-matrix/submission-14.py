class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix) # num of rows
        COLS = len(matrix[0]) # num of cols
        m = 0
        n = ROWS - 1
        # 1st BS on the matrix is to rows
        while m <= n:
            mid = m + (n-m)//2
            # now chosen the mid row

            if matrix[mid][0] > target and matrix[mid][-1] > target:
                n = mid - 1
            
            elif matrix[mid][0] < target and matrix[mid][-1] < target:
                m = mid + 1
            
            else: # its inside this row
                l = 0
                r = COLS
                while l <=r:
                    middle = l + (r-l)//2
                    if matrix[mid][middle] > target:
                        r = middle - 1
                    elif matrix[mid][middle] < target:
                        l = middle + 1
                    else:
                        return True
                return False
        
        return False