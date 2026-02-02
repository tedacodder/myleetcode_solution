class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
       
        z=set()
        for i in arr1:
            s=str(i)
            a=""
            for j in s:
                a+=j
                if a not in z:
                    z.add(a)
        ans=0
        print(a)
        
        for i in range(len(arr2)):
            x=""
            y=str(arr2[i])
            for j in range(len(y)):
                x+=y[j]
                if x in z:
                    ans=max(ans,len(x))
                else:
                    break
        return ans
                
