"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high_idx = len(nums)-1
        if target ==nums[high_idx]: return high_idx
        low_idx = 0
        while (target >= nums[low_idx])*(target <= nums[high_idx]):
            mid_idx=(low_idx+high_idx)//2
            if target ==nums[mid_idx]:
                return mid_idx
            elif target > nums[mid_idx]:
                if low_idx ==mid_idx: return -1
                low_idx = mid_idx
                continue
            else:
                high_idx = mid_idx
                continue
        return -1