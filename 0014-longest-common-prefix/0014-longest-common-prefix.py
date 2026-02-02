class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        val=sorted(strs)
        minim=val[0]
        maxi=val[-1]
        ans=""
        for i in range(min(len(minim),len(maxi))):
            if minim[i]!=maxi[i]:
                break
            ans+=minim[i]
        return ans