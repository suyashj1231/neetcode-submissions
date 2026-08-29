# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        maxSeen = root.val
        self.good = 0
        def dfs(node,maxSeen):
            if not node: return
            if node.val >= maxSeen:
                maxSeen = node.val
                self.good+=1
    
            dfs(node.left, maxSeen)
            dfs(node.right, maxSeen)

        dfs(root, maxSeen)
        return self.good