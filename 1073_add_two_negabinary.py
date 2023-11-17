"""Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array, format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

"""

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num1 = arr1[::-1]
        num2 = arr2[::-1]
        carrys = [0]*2*(max(len(num2), len(num1))+3)
        done_yet = False
        carry_quant = 0
        i = 0
        ans = []
        while not done_yet:
            done_yet = True
            digit = carrys[i]
            if i < len(num1):
                digit += num1[i]
                done_yet = False
            if i < len(num2):
                digit += num2[i]
                done_yet = False
            if digit > 0:
                ans.append(digit%2)
                digit = digit-(digit%2)
                if digit%4 == 0: carrys[i+2]+= digit//4 
                if digit%4 == 2:
                    carrys[i+2]+= digit//4 + 1
                    carrys[i+1]+= 1
                    while (carrys[i+2]>0) and (carrys[i+1]>1):
                        carrys[i+2] -=1
                        carrys[i+1] -=2
            else: ans.append(0)
            i+=1
            if done_yet:
                print(i, carrys)
                done_yet = not bool(carrys[i])
        ans = ans[::-1]
        while ans[0] == 0:
            ans.pop(0)
            if len(ans) == 0: return [0]
        return ans