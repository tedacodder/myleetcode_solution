class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        high,low=nums[-1],nums[0]
        if low<high:
            return low
        else:
            while l<r:
                mid=(l+r)//2
                if nums[r]<nums[mid]:
                    l=mid+1
                else:
                    r=mid

            return nums[l]

            