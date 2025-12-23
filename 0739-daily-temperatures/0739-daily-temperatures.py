class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)
        i=0
        while i<len(temperatures):
            if stack and temperatures[stack[-1]]<temperatures[i]:
                a=stack.pop()
                ans[a]=i-a
                continue
            else:
                stack.append(i)
            i+=1
        return ans



        