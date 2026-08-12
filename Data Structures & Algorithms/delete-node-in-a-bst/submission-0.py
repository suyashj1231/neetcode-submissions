# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        else:
            # we at deletion node 
            # case 1  - no child and case 2- 1child

            if not root.left:
                return root.right

            elif not root.right:
                return root.left
            
            else: # case 3 - 2child
            # we go 1step right and then go the left most val to find min of right tree
                curr = root.right
                while curr.left:
                    curr = curr.left
                # now out curr points to the leftmost val of right subtress
                root.val = curr.val # we assign curr val to the delted node
                # now we need to delet curr too
                root.right = self.deleteNode(root.right, curr.val) # coz we know curr in on rightside all the way to the leftmost side of right sub tree
        return root

                






        