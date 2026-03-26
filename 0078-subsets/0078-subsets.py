class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(start=0,path=[]):
            ans.append(path[:])
            if len(path)==len(nums):
                return
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack()
        return ans
        

