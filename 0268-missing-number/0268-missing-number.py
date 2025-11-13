class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        x=[i for i in range(len(nums)+1)]
        for i in range(len(nums)):
            if x[i] not in nums:
                return x[i]
        return x[-1]