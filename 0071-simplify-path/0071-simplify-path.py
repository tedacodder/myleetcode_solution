class Solution:
    def simplifyPath(self, path: str) -> str:
        files=path.split("/")
        stack=[]
        print(files)
        for f in files:
            if f=="":
                continue
            elif f=="..":
                if stack:
                    stack.pop()
            elif f==".":
                continue
            else:
                stack.append(f)
        return "/"+"/".join(stack)
