class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=[]
        i=len(digits)-1
        carry=1
        while i>=0 or carry:
            total=digits[i]+carry if i>=0 else carry
            carry=0
            if total>9:
                carry=int(str(total)[0])
                total=int(str(total)[1])  
            ans.append(total)
            i-=1
        ans.reverse()
        return ans
