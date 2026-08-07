# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0
        l_curr = l1
        r_curr = l2

        mul = 1
        while l_curr:
            
            n1+= l_curr.val * mul
            mul *= 10
            l_curr = l_curr.next

        mul = 1
        while r_curr:
            n2+= r_curr.val * mul
            mul *= 10
            r_curr = r_curr.next
        
        ans = (n1 + n2)
        if ans == 0:
            return ListNode(0)
        res = ListNode()
        ret = res

        while ans:
            digit = ans % 10
            ans = ans // 10
            res.next = ListNode(digit)
            res = res.next
        
        return ret.next

        
        