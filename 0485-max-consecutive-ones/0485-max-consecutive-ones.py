class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        globalmax=0
        i=0
        while i<len(nums):
            if nums[i]==1:
                localmax=0
                while i<len(nums) and nums[i]==1:
                    localmax+=1
                    i+=1
                globalmax=max(localmax,globalmax)
            i+=1
        return globalmax
        