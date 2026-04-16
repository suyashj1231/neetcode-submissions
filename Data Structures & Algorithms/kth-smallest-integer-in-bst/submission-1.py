# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # n=0
        # stack=[]
        # curr = root
        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
            
        #     curr = stack.pop()
        #     n+=1
        #     if n == k:
        #         return curr.val
        #     curr = curr.right

        ans = []

        def dfs(root):
            if not root: return 0

            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return ans[k-1]



