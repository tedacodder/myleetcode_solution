class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        x=[0]*(len(s)+1)
        
        ans=[]
        for i in shifts:
            direction=1
            f,e,d=i
            if d==0:
                direction=-1

            x[f]+=direction
            x[e+1]-=direction
        for g in range(1,len(s)):
            x[g]+=x[g-1]

        for i in range(len(s)):

            ans.append(chr((ord(s[i]) - ord('a') + x[i]) % 26 + ord('a')))
        return "".join(ans)
