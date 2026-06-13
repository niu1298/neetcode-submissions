# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        head = reverse(head)
        curr = head
        index = 1
        if n ==1:
            return reverse(head.next)
            
        while index != (n-1):
            curr = curr.next
            index += 1

        nxt = curr.next 
        nxt2 = curr.next.next if nxt else None

        curr.next = nxt2

        # # prev = curr
        # while curr:
        #     prev = curr
        #     curr = curr.next

        return reverse(head)