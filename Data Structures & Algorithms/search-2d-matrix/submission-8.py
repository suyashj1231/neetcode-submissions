class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        
        # Search which row could contain the target
        while left <= right:
            mid_index = (left + right) // 2
            mid_row = matrix[mid_index]
            
            # If the target is within this row's range
            if mid_row[0] <= target <= mid_row[-1]:
                # Do a binary search on the row
                return self.binary_search_in_row(mid_row, target)
            
            # If the target is greater than the last element of mid_row,
            # we move "down" (to the next rows)
            if target > mid_row[-1]:
                left = mid_index + 1
            else:
                # Otherwise, we move "up" (to the previous rows)
                right = mid_index - 1
        
        return False  # Row not found

    def binary_search_in_row(self, row: List[int], target: int) -> bool:
        left, right = 0, len(row) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
