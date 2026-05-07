class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l ,r = 0, len(matrix)-1 # sq

        while l < r:
            for i in range(r-l):
                top, btm = l, r # coz sq

                # temp val for top left
                topleft = matrix[top][l+i]

                # move btm left to top left
                matrix[top][l+i] = matrix[btm-i][l]

                # move btm right to btm left
                matrix[btm-i][l] = matrix[btm][r-i]

                # move top right to btm right
                matrix[btm][r-i] = matrix[top+i][r]

                # move temp left to top right
                matrix[top+i][r] = topleft
            
            l+=1
            r-=1
