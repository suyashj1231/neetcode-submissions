# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxdia = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if not node: return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            self.res = max(self.res, left_height+right_height)

            return 1 + max(dfs(node.left),dfs(node.right))
        
        dfs(root)
        return self.res

            
        
        