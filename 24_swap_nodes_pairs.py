"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None) or (head.next==None): return head
        return_node = head.next
        nodes = [head.next, head]
        odd_head = head
        even_head = head.next
        final = None
        while odd_head.next.next:
            odd_head.next = odd_head.next.next
            odd_head = odd_head.next
            if not even_head.next.next:
                even_head.next = None
                final = odd_head
                break
            even_head.next = even_head.next.next
            even_head = even_head.next
        odd_head.next = None
        parity = 0
        next_node = head
        while next_node:
            print("enter while", nodes[0].val, nodes[1].val)
            next_node = nodes[parity].next
            new_parity = (parity+1)%2
            nodes[parity].next = nodes[new_parity]
            nodes[parity] = next_node
            parity = new_parity
        if final: nodes[1].next = final
        return return_node
     