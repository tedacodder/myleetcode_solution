class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        z=[]
        for i in nums:
            if len(str(i))!=1:
                for j in str(i):
                    z.append(int(j))
            else:
                z.append(i)
        return z
        