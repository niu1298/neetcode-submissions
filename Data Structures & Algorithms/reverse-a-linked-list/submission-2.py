# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         ans = []
#         while head and head.next:
#             # print(head.next)
#             ans.insert(0,head.val)
#             try:
#                 head = head.next
#             except:
#                 break
#         if head:
#             ans.insert(0,head.val)
        
#         dummy = ListNode(0)
#         curr = dummy

#         for num in ans:
#             curr.next = ListNode(num)
#             curr = curr.next

#         return dummy.next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev