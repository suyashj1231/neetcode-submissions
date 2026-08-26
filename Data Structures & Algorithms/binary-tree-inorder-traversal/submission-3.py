from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack = []
        res = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                value = stack.pop()
                res.append(value.val)
                curr = value.right
        
        return res


