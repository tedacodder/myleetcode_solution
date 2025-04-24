class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x=nums1.copy()
        x.extend(nums2)
        x.sort()
        if len(x)%2==0:
            return (x[len(x)//2]+x[len(x)//2-1])/2
        else:
            return x[len(x)//2]


        