'''
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        '''
        BRUTE FORCE
        - traverse all the linked lists and save the values in a list
        - sort the list
        - create a new sorted linked list
        
        Time complexity : O(NlogN) where N is the total number of nodes.
            Collecting all the values costs O(N) time.
            A stable sorting algorithm costs O(NlogN) time.
            Iterating for creating the linked list costs O(N) time.
            
        Space complexity : O(N).
            Sorting cost O(N) space (depends on the algorithm you choose).
            Creating a new linked list costs O(N) space.
        '''
        nodes = [] # empty list to store the values
        
        head = point = ListNode(0) # new ListNode to save sorted nodes

        for l in lists: # loop all the linked list in lists
            while l: # if there is one
                nodes.append(l.val) # save the value to nodes
                l = l.next # move to the next node
        
        for x in sorted(nodes): # sort nodes and loop its values
            point.next = ListNode(x) # make a node of x and save to the new linked list using point
            point = point.next # move point to next node
        
        return head.next


        '''
        Priority Queue

        Time complexity : O(Nlogk) where k is the number of linked lists.
            The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue.
            But finding the node with the smallest value just costs O(1) time.
            There are N nodes in the final linked list.
        Space complexity :
            O(n) Creating a new linked list costs O(n) space.
            O(k) The code above present applies in-place method which cost O(1)O(1)O(1) space.
            And the priority queue (often implemented with heaps) costs O(k)O(k)O(k) space (it's far less than N in most situations).
        '''
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        head = point = ListNode(0)

        q = PriorityQueue()

        for l in lists:
            if l:
                q.put(Wrapper(l))

        while not q.empty():
            node = q.get().node
            point.next = node
            point = point.next
            node = node.next
            if node:
                q.put(Wrapper(node))

        return head.next


        '''
        Divide And Conquer
        - Pair up k lists and merge each pair.
        - After the first pairing, k lists are merged into k/2 lists with average 2N/k length, then k/4, k/8 and so on.
        - Repeat this procedure until we get the final sorted linked list.
        '''

        # create a function to merge 2 lists
        def merge2Lists(self, l1, l2):
            head = point = ListNode(0)

            while l1 and l2:
                if l1.val <= l2.val:
                    point.next = l1
                    l1 = l1.next
                else:
                    point.next = l2
                    l2 = l1
                    l1 = point.next.next
                point = point.next

            if not l1:
                point.next=l2
            else:
                point.next=l1

            return head.next

        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if amount > 0 else None