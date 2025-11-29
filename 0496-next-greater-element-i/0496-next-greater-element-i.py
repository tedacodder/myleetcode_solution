class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums1)
        a=0
        for i in nums1:
            
            for j in range(nums2.index(i)+1,len(nums2)):
                if nums2[j]>i:
                    ans[a]=nums2[j]
                    break
                
            a+=1
        return ans                        




        