# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSametree(self,r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if not r and not s:
            return True
        if not r or not s:
            return False
        if r.val != s.val:
            return False
        
        left = self.isSametree(r.left, s.left)
        right = self.isSametree(r.right, s.right)
        return left and right

    def isSubtree(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if not r: return False
        if not s: return True
        if self.isSametree(r,s):
            return True
        
        return (self.isSubtree(r.left,s) or self.isSubtree(r.right,s))
        