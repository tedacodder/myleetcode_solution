class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        x=list(set(nums))
        element = x[0]
        count=0
        for i in x:
            if nums.count(i)>count:
                count=nums.count(i)
                element=i
        return element

        