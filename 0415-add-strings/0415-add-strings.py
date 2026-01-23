class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry=0
        i=len(num1)-1
        j=len(num2)-1
        ans=[]
        while i>=0 or j>=0 or carry:
            a=int(num1[i]) if i>=0 else 0
            b=int(num2[j]) if j>=0 else 0
            total=a+b+carry
            carry=0
            if total >9:
                carry=int(str(total)[0])
                total=int(str(total)[1])
            ans.append(str(total))
            i-=1
            j-=1
        return "".join(reversed(ans))
        