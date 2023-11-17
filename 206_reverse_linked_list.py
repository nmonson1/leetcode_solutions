"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = [head]
        if head == None: return None
        while nodes[-1].next != None:
            nodes.append(nodes[-1].next)
        rev_nodes = nodes[::-1]
        for idx, node in enumerate(rev_nodes):
            if idx+1 == len(rev_nodes):
                rev_nodes[idx].next = None
            else:
                rev_nodes[idx].next = rev_nodes[idx+1]
        return rev_nodes[0]