class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack=[]
        ans=""
        for i in range(len(word)):
            if word[i]==ch:
                ans+=ch
                stack.reverse()
                val="".join(stack)
                ans+=val
                ans+=word[i+1:]
                stack=[]
                break

            else:
                stack.append(word[i])
        return ans+"".join(stack)
        