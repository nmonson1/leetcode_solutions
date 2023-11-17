"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        local_maxes = []
        current_best = (0,0)
        water_vols=[]
        current_vol = 0
        l = len(height)
        for idx, alt in enumerate(height):
            if alt<current_best[1]:
                current_vol+=current_best[1]-alt
            else:
                current_best = idx, alt
                local_maxes.append(current_best)
                water_vols.append(current_vol)
                current_vol = 0
        idx_of_max = current_best[0]
        current_best = (0,0)
        current_vol = 0
        for idx in range(l-idx_of_max):
            idx = l-idx-1
            alt = height[idx]
            if height[idx] < current_best[1]:
                current_vol += current_best[1] - alt
            else:
                current_best = idx, alt
                local_maxes.append(current_best)
                water_vols.append(current_vol)
                current_vol = 0
        return sum(water_vols)