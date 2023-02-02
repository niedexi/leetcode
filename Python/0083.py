'''
83. Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or head.next: return head
        slow = head
        fast = head

        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next

        slow.next = None
        return head


        # sample answer
        if not head or not head.next:
            return head
        prev=head
        ptr=head.next
        while(ptr):
            while(ptr and ptr.val==prev.val):
                ptr=ptr.next
            prev.next=ptr
            prev=ptr
            if ptr:
                ptr=ptr.next
        return head


        # sample answer
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

        #sample
        cur=head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur=cur.next
        return head