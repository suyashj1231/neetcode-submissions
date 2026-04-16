# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def samedfs(p,q):
            if not p and not q: # none node
                return True
            
            if p and q and p.val == q.val: # if same and non empty
                left = samedfs(p.left, q.left)
                right = samedfs(p.right, q.right)
                return left and right
            
            # if both of these don't execute
            # so 1 tree is empty and 1 is not empty
            return False
    
        if not subRoot: return True
        if not root: return False
        if samedfs(root, subRoot):
            return True
        # but if they are not the same tree, compare t with left subtree of s 
        # and compare t with right subtree of s

        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))
    
            

    


