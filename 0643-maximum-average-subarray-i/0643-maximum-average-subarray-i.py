class Solution:
    def subarray(self,arr,k):
        windowSum=sum(arr[:k])
        ans=[windowSum]
        for i in range(k,len(arr)):
            windowSum+=arr[i]-arr[i-k]
            ans.append(windowSum)
        return ans

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        x=self.subarray(nums,k)
        print(x)
        return max(x)/k
        