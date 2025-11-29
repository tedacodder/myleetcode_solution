# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #2try
        a=1
        b=n
        bad=0
        while a<=b:
            mid=(a+b)//2
            if isBadVersion(mid):
                bad=mid
                b=mid-1
            else:
                a=mid+1
        return bad

        