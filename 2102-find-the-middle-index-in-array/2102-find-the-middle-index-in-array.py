class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        prefix_sum = 0

        # Build prefix sum
        for i in range(len(nums)):
            prefix_sum += nums[i]
            prefix[i] = prefix_sum

        total = prefix[-1]

        for i in range(len(nums)):
            left_sum = 0 if i == 0 else prefix[i - 1]
            right_sum = total - prefix[i]

            if left_sum == right_sum:
                return i

        return -1
