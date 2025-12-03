class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #two pointer finder and seeker
        s=[]
        l=0
        r=0
        count=0
        for i in range(len(nums)):
            if nums[i] not in s:
                nums[i],nums[l]=nums[l],nums[i]
                s.append(nums[l])
                l+=1
        return len(s)

            


           
            

       