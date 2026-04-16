# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2
        carry = 0
        ans = ""
        dmy = new_head = ListNode(0)

        while first or second or carry:
            if first:
                val1 = first.val
                first = first.next
            else:
                val1 = 0

            if second:
                val2 = second.val
                second = second.next
            else:
                val2 = 0
            temp_sum = val1 + val2 + carry
            carry = temp_sum// 10
            digit = temp_sum % 10

            new_head.next = ListNode(digit)            
            new_head = new_head.next
        
        return dmy.next

        
        

        
