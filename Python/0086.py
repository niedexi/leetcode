'''
86. Partition List

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        less = ListNode() # store nodes less than x
        greater = ListNode() # store nodes greater than x

        # pointers for generating the nodes
        pl = less
        pg = greater

        p = head # for traversing original ListNode

        while p:
            if p.val >= x: # val greater than x
                pg.next = p # put node in pg 
                pg = pg.next # pg moves to next
            else:
                pl.next = p # put node in pl
                pl = pl.next # pl moves to next
            
            temp = p.next
            p.next = None
            p = temp
        
        pl.next = greater.next # put two half ListNode back together
        return less.next