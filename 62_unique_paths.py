"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d={(0,0):1}
        mind, maxd = min(m,n), max(m,n)
        for dist in range(1,maxd+mind-1):
            for i in range(0,dist+1):
                j = dist-i
                if (i<maxd) and (j<mind):
                    print("added", i, j, dist)
                    ans = 0
                    if i>0: ans+=d[(i-1,j)]
                    if j>0: ans+=d[(i,j-1)]
                    d[(i,j)] =ans
        return d[(maxd-1, mind-1)]

