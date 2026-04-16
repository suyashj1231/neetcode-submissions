# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        first_arr = ""
        sec_arr = ""

        while l1 or l2:
            if l1:
                first_arr = first_arr + str(l1.val)
                l1 = l1.next
            
            if l2:
                sec_arr = sec_arr + str(l2.val)
                l2 = l2.next
        
        first_arr = first_arr[::-1]
        sec_arr = sec_arr[::-1]
        print(first_arr,sec_arr)
        final = int(first_arr) + int(sec_arr)
        final = str(final)[::-1]

        new_head = ListNode(int(final[0]))
        current = new_head

        for i in range(1, len(final)):
            current.next = ListNode(int(final[i]))
            current = current.next

        return new_head
