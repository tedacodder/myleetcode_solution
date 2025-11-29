class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cur_sum=0
        index=0
        patch=0
        while index<len(nums) and cur_sum<n:
            if nums[index]<=cur_sum  + 1:
                cur_sum+=nums[index]
                index+=1
            else:
                
                patch+=1
                cur_sum+=cur_sum+1
        while cur_sum<n:
            patch+=1
            cur_sum+=cur_sum+1
        return patch

        