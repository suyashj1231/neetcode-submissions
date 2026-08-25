"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack = [(root,False)]
        res = []

        while stack:
            curr, visited = stack.pop()
            if visited:
                res.append(curr.val)
            else:
                stack.append((curr, True))
                for child in curr.children[::-1]:
                    stack.append((child, False))

        return res

        