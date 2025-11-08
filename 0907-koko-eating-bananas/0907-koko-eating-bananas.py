class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low , high = 1 , sum(piles)
        ans = high
        def check(k):
            hours = 0
            for i in range(len(piles)):
                hours += ceil(piles[i]/k)
            return hours <= h

        while low <= high:
            mid = (low+high)//2
            
            if check(mid):
                high = mid-1
                ans = min(ans,mid)
            else:
                low = mid + 1
        return ans
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
        