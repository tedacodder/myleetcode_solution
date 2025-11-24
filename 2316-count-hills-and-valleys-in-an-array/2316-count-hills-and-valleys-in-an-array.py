class Solution:
    def countHillValley(self, nums: List[int]) -> int:
       # Step 1: remove consecutive duplicates
        arr = [nums[0]]
        for x in nums[1:]:
            if x != arr[-1]:
                arr.append(x)

        count = 0

        # Step 2: count hills and valleys
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                count += 1  # hill
            if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                count += 1  # valley

        return count