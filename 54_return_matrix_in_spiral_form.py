"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

def rem_top(matrix):
    ans = matrix.pop(0)
    return ans
def rem_right(matrix):
    #num_rows = len(matrix)
    ans = []
    for row in matrix:
        ans+=[row.pop(-1)]
    return ans
def rem_left(matrix):
    ans = []
    for row in matrix:
        ans+=[row.pop(0)]
    ans.reverse()
    return ans
def rem_bot(matrix):
    ans = (matrix.pop(-1))
    ans.reverse()
    return ans
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        ans = []
        dir = -1
        while (rows>0) and (cols>0):
            dir=(dir+1)%4
            if dir%2 ==0: rows-=1
            else: cols -=1
            if dir == 0: ans+=rem_top(matrix)
            elif dir == 1: ans+=rem_right(matrix)
            elif dir == 2: ans+=rem_bot(matrix)
            else: ans += rem_left(matrix)
            print(dir, ans, matrix)
        return ans