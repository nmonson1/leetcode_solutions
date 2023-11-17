#Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        full_str_len =len(s) 
        beg_idx = 0
        leng = 0
        print(s)
        while beg_idx + leng < full_str_len:
            #print(beg_idx, leng)
            repeat_set = set(i for i in s[beg_idx:beg_idx+leng] if s[beg_idx:beg_idx+leng].count(i)>1)
            #print(repeat_set)
            if len(repeat_set) > 0:
                beg_idx = max([s.rfind(r, beg_idx, s.rfind(r, beg_idx, beg_idx+leng)) for r in repeat_set])
                beg_idx+=1
                print()
                print(repeat_set, beg_idx)
                continue
            elif s[beg_idx + leng] in s[beg_idx:beg_idx + leng]:
                beg_idx+=1
                continue
            else:
                leng +=1
        return leng