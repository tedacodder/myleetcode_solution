class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return bisect.bisect_left(nums,target)
        return -1
        