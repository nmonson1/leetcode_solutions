"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        initial_node = ListNode(0)
        current_node = initial_node
        while (l1 != None and l2 != None):
            current_node.val = (l1.val+l2.val+carry)%10
            current_node.next = ListNode(0)
            prev_node = current_node
            current_node = current_node.next
            carry = 1 if (l1.val+l2.val+carry>9) else 0
            l1 = l1.next
            l2 = l2.next
        if l1 == None:
            l1 = l2
        while l1 != None:
            current_node.val = (l1.val+carry)%10
            current_node.next = ListNode(0)
            prev_node = current_node
            current_node = current_node.next
            carry = 1 if (l1.val+carry>9) else 0
            l1 = l1.next
        if carry ==1:
            current_node.val = carry
        else:
            prev_node.next=None
        return initial_node