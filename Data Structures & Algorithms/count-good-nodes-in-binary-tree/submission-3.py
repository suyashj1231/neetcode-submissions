from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        q = deque()
        q.append([root,float('-inf')])
        good_nodes = 0

        while q:
            node, max_till_here = q.popleft()
            if node.val >= max_till_here:
                good_nodes+=1
                max_till_here = node.val
            
            if node.left:
                q.append([node.left, max_till_here])
            if node.right:
                q.append([node.right, max_till_here])
        
        return good_nodes
                


