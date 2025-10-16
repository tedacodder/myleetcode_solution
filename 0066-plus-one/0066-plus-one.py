class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=[str(i) for i in digits]
        x="".join(x)
        x=int(x)
        x+=1
        z=[int(j) for j in str(x)]
        return z