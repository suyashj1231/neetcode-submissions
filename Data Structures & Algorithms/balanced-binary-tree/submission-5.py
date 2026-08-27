# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=, Self0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True
        def dfs(root):
            if not root: return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            if abs(right_height - left_height) > 1:
                self.balance = False
            
            return 1 + max(dfs(root.left),dfs(root.right))
    
        dfs(root)
        return self.balance
                
