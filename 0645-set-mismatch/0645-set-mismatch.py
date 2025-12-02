class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        f=1
        #two pointer technique
        l=0
        r=1
        while r<len(nums):
            if nums[l]==nums[r]:
                a=nums[l]
                break
            l+=1
            r+=1

        for i in nums:
            if f not in nums:
                b=f
                break
            f+=1
        return [a,b]

        