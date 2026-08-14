"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cpy = head
        random = {None: None}
        while cpy:
            random[cpy] = Node(cpy.val)
            cpy = cpy.next

        new_head = Node(0)
        curr = new_head

        while head:
            curr.next = random[head]
            curr.next.random = random[head.random]
            head = head.next
            curr = curr.next
        
        return new_head.next
        
