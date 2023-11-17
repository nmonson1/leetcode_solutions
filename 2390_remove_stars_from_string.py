"""
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
"""

class Solution:
    def removeStars(self, s: str) -> str:
        length = len(s)
        idx = 0
        while (idx+1)<len(s):
            if s[idx+1] == "*":
                if idx+2<len(s):
                    s = s[0:idx]+s[idx+2:]
                else: return s[0:idx]
                idx -=1
                continue
            idx+=1
        return s
            