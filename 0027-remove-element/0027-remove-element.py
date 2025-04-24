class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=0
        while a!=len(nums):
            if nums[a]==val:
                nums[a],nums[-1]=nums[-1],nums[a]
                nums.pop()
            else:
                a+=1

        return len(nums)