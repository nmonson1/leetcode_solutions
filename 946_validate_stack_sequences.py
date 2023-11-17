"""
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

"""

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [-1]
        length = len(pushed)
        push_idx = 0
        pop_idx = 0
        while pop_idx < length:
            if stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx+=1
                continue
            else:
                if push_idx == length: return False
                stack.append(pushed[push_idx])
                push_idx+=1
        return True