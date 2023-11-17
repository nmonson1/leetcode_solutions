"""
You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.
"""

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        num_col = len(colSum)
        num_rows = len(rowSum)
        matrix = [colSum[:]]
        idx = 0
        for i in range(num_rows-1):
            matrix.append([0]*num_col)
            while sum(matrix[i+1])<rowSum[i+1]:
                target_shift_amt = rowSum[i+1]-sum(matrix[i+1])
                shift_amt = min(target_shift_amt, matrix[0][idx])
                matrix[0][idx] -= shift_amt
                matrix[i+1][idx] += shift_amt
                if matrix[0][idx] ==0: idx+=1
        return matrix