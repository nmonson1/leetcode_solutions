#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        gen = 0
        ans = [["", 0, 0]] #paren string, signature = num ( -num ), num (
        while gen < 2*n:
            print(gen, [s[0] for s in ans] )
            for i in range(len(ans)):
                s=ans[i]
                if s[1]==0:
                    s[0]+="("
                    s[1]+=1
                    s[2]+=1
                elif s[2] ==n:
                    s[0]+=")"
                    s[1]-=1
                else:
                    s1 = [s[0]+"(", s[1]+1, s[2]+1]
                    s[0]+=")"
                    s[1]-=1
                    ans.append(s1)
            gen+=1
        return [s[0] for s in ans]