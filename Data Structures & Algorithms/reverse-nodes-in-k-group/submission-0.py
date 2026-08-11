# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prevGrp = dummy

        while True:
            kth = self.getKth(prevGrp,k)
            if not kth:
                break
            # right after grp
            nextGrp = kth.next

            # reverse
            prev, curr = kth.next, prevGrp.next
            while curr != nextGrp:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            temp = prevGrp.next
            prevGrp.next = kth
            prevGrp = temp
        return dummy.next
    
    def getKth(self, node,k):
        while node and k>0:
            node = node.next
            k = k-1
        return node

