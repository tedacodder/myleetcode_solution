class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        x=""
        for i,s in count.most_common():
            x+=i*s
        
        return x

        