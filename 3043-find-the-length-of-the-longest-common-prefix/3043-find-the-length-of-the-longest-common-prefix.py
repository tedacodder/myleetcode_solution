class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1.sort()
        
        z={}
        for i in arr1:
            s=str(i)
            a=""
            for j in s:
                a+=j
                if a not in z:
                    z[a]=len(a)
        ans=0
        
        for i in range(len(arr2)):
            x=""
            y=str(arr2[i])
            for j in range(len(y)):
                x+=y[j]
                if x in z:
                    ans=max(ans,z[x])
                else:
                    break
        return ans
                
