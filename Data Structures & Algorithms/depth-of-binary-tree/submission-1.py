from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        stack = [[root, 1]]
        result = 0

        while stack : 
            node, depth = stack.pop()

            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return result
        
        
        
        # if not root:return 0
        # q = deque([root])
        # length = 0
        # while q:
        #     for _ in range(len(q)):
        #         element = q.popleft()
        #         if element.left:
        #             q.append(element.left)
                
        #         if element.right:
        #             q.append(element.right)
            
        #     length += 1
        
        # return int(length)

        
        # if not root:return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))