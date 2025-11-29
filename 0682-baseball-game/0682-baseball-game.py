class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            last=len(stack)-1
            if "C" ==i:
                stack.pop()
            elif "D"==i:
                stack.append(stack[last]*2)
            elif "+"==i:
                stack.append(stack[last]+stack[last-1])
            else:
                stack.append(int(i))
        return sum(stack)
            
        