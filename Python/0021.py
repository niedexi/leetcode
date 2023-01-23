'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # check if one list is empty return the other one.
        if not list1: return list2
        if not list2: return list1

        # create a new empty ListNode with an empty head to store the result, use po to track current position.
        po = dummy = ListNode()

        while list1 and list2: # check if both list not empty
            if list1.val < list2.val: # if list1 value is smaller
                po.next = list1 # insert list1 to the new list
                list1 = list1.next # list1 moves to the next value
            else:
                po.next = list2 # else insert list2 value to the new list
                list2 = list2.next # list2 moves to the next vlue

            po = po.next # advance the position
        
        # after the while loop finishes check if there is still remaining elements left.
        if list1:
            po.next = list1
        if list2:
            po.next = list2

        return dummy.next




# def mergeTwoLists(self, l1, l2):
#     if not l1: return l2
#     if not l2: return l1

#     if (l1.val < l2.val):
#     	l1.next = mergeTwoLists(l1.next, l2)
#       return l1
#     else:
#     	l2.next = mergeTwoLists(l2.next, l1)
#     	return l2
    	