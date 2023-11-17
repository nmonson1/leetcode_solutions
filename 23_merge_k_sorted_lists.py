"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class goodSolution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        num_lists = len(lists)
        next_node = ListNode()
        while num_lists != 0:
            
            next_val = min(lists)
            next_node.val = next_val
            
            next_node = 1

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        total_list = []
        num_elem = 0
        for i in range(len(lists)):
            while lists[i] != None:
                total_list.append(lists[i].val)
                num_elem+=1
                lists[i]=lists[i].next
        total_list.sort()
        next_node = ListNode()
        initial_node = ListNode(0, next_node)
        for value in total_list:
            next_node.val = value
            prev_node = next_node
            next_node = ListNode()
            num_elem-=1
            if num_elem:
                prev_node.next = next_node
            else: return initial_node.next