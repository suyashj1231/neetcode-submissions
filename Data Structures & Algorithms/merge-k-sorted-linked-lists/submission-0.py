# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            new_round = []
            for i in range(0, len(lists), 2):
                a = lists[i]
                b = lists[i+1] if (i+1) < len(lists) else None
                c = head =ListNode(0)
                while a and b:
                    if a.val > b.val:
                        head.next = b
                        b = b.next
                    else:
                        head.next = a
                        a = a.next
                    head = head.next
                while a:
                    head.next = a
                    a = a.next
                    head = head.next
                
                while b:
                    head.next = b
                    b = b.next
                    head = head.next
                new_round.append(c.next)
            lists = new_round

        if not lists or len(lists) == 0:
            return None
        return lists[0]




            
        