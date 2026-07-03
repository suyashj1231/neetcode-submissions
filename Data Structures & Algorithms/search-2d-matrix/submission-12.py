class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrixnew = []

        for row in matrix:
            matrixnew.extend(row)
        l = 0
        r = len(matrixnew) - 1

        while l <= r:
            mid = l + (r-l)//2
            print(mid)
            if matrixnew[mid] > target:
                r = mid - 1
            elif matrixnew[mid] < target:
                l = mid + 1
            else:
                return True

        return False