class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def ispow(x):
            if x==1:
                return True
            elif x<=0 or x%4!=0:
                return False
            return ispow(x//4)
        return ispow(n)
