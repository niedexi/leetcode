'''
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # 1
        dummy = ListNode(0)
        dummy.next = head

        p1, p2 = dummy, dummy

        for i in range(n + 1):
            p1 = p1.next

        while p1:
            p2 = p2.next
            p1 = p1.next
        
        p2.next = p2.next.next

        return dummy.next

        # 2
        l, r = head, head
        for i in range(n):
            r = r.next
        if not r:
            return head.next
        while r.next:
            l = l.next
            r = r.next
        l.next = l.next.next
        return head