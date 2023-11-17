"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        another = head.next
        if another == None: return None
        nodes = [head]
        while another:
            nodes.append(another)
            next_node = another
            another = next_node.next
        if n == len(nodes): return nodes[1]
        nodes[len(nodes)-n-1].next = nodes[len(nodes)-n].next
        return nodes[0]