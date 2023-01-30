'''
25. Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # recursive
        def reverse(a, b):
            prev = None
            curr = a

            while curr != b:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return prev

        if not head: return head
        a = head
        b = head

        for i in range(k):
            if not b: return head
            b = b.next
        
        newHead = reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead