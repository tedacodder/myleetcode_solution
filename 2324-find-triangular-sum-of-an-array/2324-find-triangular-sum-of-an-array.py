class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        ans=[]
        ans.append(nums)
        for i in range(len(nums),1,-1):
            a=[]
            l=0
            r=1
            
            while r<i:
                z=(ans[-1][l]+ans[-1][r])%10
                a.append(z)
                l+=1
                r+=1
            ans.append(a)
        return ans[-1][0]


        