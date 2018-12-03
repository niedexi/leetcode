'''
Merge two sorted linked lists and return it as a new list. The new list should 
be made by splicing together the nodes of the first two lists.

Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''

def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1: return l2
    if not l2: return l1

    if (l1.val < l2.val):
    	l1.next = mergeTwoLists(l1.next, l2)
    	return l1
    else:
    	l2.next = mergeTwoLists(l2.next, l1)
    	return l2
    	