class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        cur = nums
        
        # Reduce nums until only one element left
        while len(cur) > 1:
            nxt = []
            for i in range(len(cur) - 1):
                nxt.append((cur[i] + cur[i + 1]) % 10)
            cur = nxt
        
        return cur[0]


        