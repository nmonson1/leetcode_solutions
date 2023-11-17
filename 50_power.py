#Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        power2n = x
        powers2 = []
        for i in range(n.bit_length()):
            powers2.append(power2n)
            power2n *= power2n
        print(powers2)
        ans = 1
        idx = -1
        for d in bin(n)[::-1]:
            idx+=1
            if d == "b": return ans
            if d=="0": continue
            ans*=powers2[idx]