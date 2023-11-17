"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

"""

def standard_form(frac):
    y = frac[0]
    x = frac[1]
    was_neg = bool(y<0) ^ bool(x<0)
    if y == 0: return (0,1)
    elif x == 0: return (1,0)
    else:
        a1 = abs(x)
        a2 = abs(y)
        while a1 !=0:
            remain = a1
            quotient, a1 = divmod(a2, a1)
            a2 = remain
    if was_neg: return (-1*abs(y//a2), abs(x//a2))
    return (abs(y//a2), abs(x//a2))

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<3: return len(points)
        print(len(points))
        best_case = 0
        for p_idx, p in enumerate(points):
            d = {}
            for q_idx, q in enumerate(points):
                if q_idx == p_idx: continue
                slope = standard_form((p[1]-q[1], p[0]-q[0]))
                if slope in d:
                    d[slope]+=1
                else: d[slope]=1
            if max(d.values()) > best_case: best_case = max(d.values())
        return best_case+1