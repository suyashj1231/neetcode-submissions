# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #1,2,3,4,5 remove n = 2 so len - 2 = 3 position (4)
        # fast = 1 (3) --> (4) --> (5)
        # slow = 0 (1) --> 2 --> 3 ,slow.next should be removed
        dum = ListNode(0, head)
        first = second = dum

        for _ in range(n+1):
            first = first.next
        
        # now first is at n and second at head
        # move both together to the end
        while first:
            first = first.next
            second = second.next
        
        # second.next to be removed
        new = second.next.next
        second.next = second.next.next

        return dum.next


        

