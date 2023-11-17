#Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_length = 1
        best_p = s[0]
        length = len(s)
        #check even lengths
        for idx, char in enumerate(s):
            half_length = 0
            while idx-half_length >= 0 and idx + half_length+1 < length and s[idx-half_length] == s[idx+half_length+1]:
                half_length+=1
                #print("case1", idx, char, half_length)
                if half_length*2 > best_length:
                    best_length = half_length*2
                    best_p = s[idx-half_length+1: idx+half_length+1]
                 #   print("updated")
        #check odd lengths
        for idx, char in enumerate(s):
            half_length = 0
            while idx-half_length >= 0 and idx + half_length < length and s[idx-half_length] == s[idx+half_length]:
                if (half_length*2) + 1 > best_length:
                  #      print("checked odd", half_length)
                        best_length = half_length*2 + 1
                        best_p = s[idx-half_length: idx+half_length+1]
                half_length +=1
        return best_p