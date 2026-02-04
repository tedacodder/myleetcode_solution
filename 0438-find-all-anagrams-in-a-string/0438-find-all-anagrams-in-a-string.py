class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        x=Counter(s[:k])
        check=Counter(p)
        ans=[]
        if x==check:
            ans.append(0)
        for i in range(k,len(s)):
            x[s[i]]+=1
            x[s[i-k]]-=1
            if x==check:
                ans.append(i-k+1)
        return ans



