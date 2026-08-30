"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            same = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        same = False
                        break
            if same:
                return Node(grid[r][c], True)

            n = n // 2
            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c+n)
            btmLeft = dfs(n, r+n, c)
            btmRight = dfs(n, r+n, c+n)

            return Node(grid[r][c], False, topLeft, topRight, btmLeft, btmRight)

        return dfs(len(grid), 0, 0)
            
            


                    


            




        
