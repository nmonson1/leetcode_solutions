"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(enumerate(nums), key=lambda i: i[1])
        lower_idx = 0
        upper_idx = len(nums)-1
        current_sum = nums[lower_idx][1] + nums[upper_idx][1]
        while current_sum != target:
            if target < current_sum:
                upper_idx -= 1
            elif target > current_sum:
                lower_idx += 1
            current_sum = nums[lower_idx][1] + nums[upper_idx][1]
        return [nums[lower_idx][0], nums[upper_idx][0]]