# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minNode(self, node: Optional[TreeNode]):
        while node and node.left:
            node = node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val:
           root.left = self.deleteNode(root.left, key)
        
        else: # root = target
            if not root.left:
                return root.right
                
            elif not root.right:
                return root.left

            else: 
                # TODO: Find the min val in the right. subtree
                # replace them
                # recersive delete this original copy
                minvalue = self.minNode(root.right)
                root.val = minvalue.val
                root.right = self.deleteNode(root.right, minvalue.val)
        return root



