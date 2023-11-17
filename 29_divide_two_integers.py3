"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        initial_dif = dividend.bit_length()-divisor.bit_length()  
        was_neg = (dividend < 0)+(divisor < 0)
        if dividend < 0: dividend = -dividend
        if divisor < 0: divisor = -divisor
        if initial_dif>30 and was_neg==1:
            return -1<<31
        elif initial_dif>30:
            return (1<<31)-1

        count = 0
        while dividend>=divisor:
            dif = dividend.bit_length()-divisor.bit_length()
            if dividend-(divisor<<dif)>=0:
                count+=2**dif
                dividend = dividend-(divisor<<dif)
                continue
            else:
                count+=2**(dif-1)
                dividend = dividend-(divisor<<(dif-1))
                continue
        if was_neg==1: return -count
        return count