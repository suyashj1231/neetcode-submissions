# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        node = root

        while stack or node:
            if node:
                stack.append([node, 0]) # u passed through it once
                node = node.left
            else:
                curr, state = stack.pop()
                if state == 0: # seen again so now we can add it res if again seen
                    state = 1
                    stack.append([curr, state])
                    node = curr.right
                else:
                    res.append(curr.val)
        
        return res





