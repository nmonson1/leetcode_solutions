"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        initial = x
        reverse = 0
        while x>0:
            reverse*=10
            print(x,reverse)
            q,r = divmod(x,10)
            x=q
            reverse+=r
            
        return bool(initial==reverse)