class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        currsum = 0
        dic={0:1}
        for i in nums:
            currsum+=i
            if currsum-k in dic:
                count+=dic[currsum-k]
            dic[currsum]=dic.get(currsum,0)+1
        return count