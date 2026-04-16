# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # now slow would be at middle and fast at end
        # reverse a pointer

        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

# merge the 2 falfs
        second = prev # second was null and prev was before it
        first = head
        while second:
            tmp_f = first.next
            tmp_s = second.next
            first.next = second
            second.next = tmp_f
            first = tmp_f
            second = tmp_s



