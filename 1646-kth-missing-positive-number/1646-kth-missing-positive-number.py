class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        a=1
        count=0
        while count!=k:
            if a not in arr:
                count+=1
            a+=1
        return a-1


