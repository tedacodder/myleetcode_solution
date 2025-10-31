class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        count=0
        window=Counter(s[:3])
        def add(window,s):
            if s in window:
                window[s]+=1
            else:
                window[s]=1
        def remove(window,s):
            if window[s]==1:
                del window[s]
            else:
                window[s]-=1
        if len(window)==3:
            count+=1  
        for i in range(3,len(s)):
            
            #add
            add(window,s[i])

            #delete 
            remove(window,s[i-3])
            if len(window)==3:
                count+=1
        return count


        