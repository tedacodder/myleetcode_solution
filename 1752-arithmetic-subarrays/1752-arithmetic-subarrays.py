class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        ans=[]
        for i,j in zip(l,r):
            a=True
            left=0
            right=1
            sub = nums[i:j+1]
            sub.sort()
            d=sub[1]-sub[0]
            while right <len(sub):
                if sub[right]-sub[left]!=d:
                    a=False
                    break
                right+=1
                left+=1
            ans.append(a)
        return ans
        
            

        