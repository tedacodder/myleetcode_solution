class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(1,numRows+1):
            a=[1]*i
            if len(ans)>=2:
                b=ans[-1]
                l=0
                r=1
                k=1
                while r<len(b):
                    a[k]=b[l]+b[r]
                    l+=1
                    r+=1
                    k+=1
            ans.append(a)
        return ans
                

        