class Solution:
    def isValid(self, s: str) -> bool:
        dic={"}":"{",")":"(","]":"["}
        stack=[]
        for i in s:
            if i in dic:
                if len(stack)==0:
                    return False
                else:
                    if dic[i]==stack[-1]:
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(i)
        return len(stack)==0

