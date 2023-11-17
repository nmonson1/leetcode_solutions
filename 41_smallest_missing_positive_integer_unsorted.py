"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maxlength = len(nums)
        nums = [0]+nums
        ans = 0
        for idx, num in enumerate(nums):
            if (num < 0) or (num > maxlength) or (num == idx):
                continue
            else:
                next_num = num
                while (next_num>0) and (next_num<=maxlength) and (nums[next_num] !=next_num) :
                    num = next_num
                    next_num = nums[num]
                    nums[num] = num
        print(nums)
        while ans< maxlength+1 and nums[ans] == ans:
            ans+=1   
        return ans

