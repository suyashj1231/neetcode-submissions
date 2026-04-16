from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # dfs
        # queue = deque()
        # if root:
        #     queue.append(root)

        # level = 0

        # while queue:
        #     for i in range(len(queue)):
        #         curr = queue.popleft()

        #         if curr.left:
        #             queue.append(curr.left)
                
        #         if curr.right:
        #             queue.append(curr.right)

        #     level += 1
        
        # return level

        # idfs
        if not root:
            return 0
        stack = [[root, 1]]
        res = 0
        while stack:
            node, height = stack.pop()
            if node: # if not null
                res = max(res, height)
                stack.append([node.left, height + 1])
                stack.append([node.right, height + 1])
        
        return res

        


        



