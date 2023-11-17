"""
You are given an integer num. You will apply the following steps exactly two times:

Pick a digit x (0 <= x <= 9).
Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
Replace all the occurrences of x in the decimal representation of num by y.
The new integer cannot have any leading zeros, also the new integer cannot be 0.
Let a and b be the results of applying the operations to num the first and second times, respectively.

Return the max difference between a and b.
"""

class Solution:
    def maxDiff(self, num: int) -> int:
        str_digits = str(num)
        num_digits = len(str_digits)

        a = str_digits
        b = str_digits
        for idx, i in enumerate(str_digits):
            if idx ==0:
                if i !="1":
                    a = str_digits.replace(i,"1")
                    break
            elif (i != "0") and (i !=str_digits[0]):
                a = str_digits.replace(i,"0")
                break
        for i in str_digits:
            if i !="9":
                b = str_digits.replace(i,"9")
                break
        print(a,b)
        return int(b)-int(a)