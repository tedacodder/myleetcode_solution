class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=0
        b=len(s)-1
        while a<=b:
            if (s[a].isalpha() or s[a].isdigit()) and (s[b].isalpha() or s[b].isdigit()):
                if s[a].lower()!=s[b].lower():
                    return False
                a+=1
                b-=1
            
            elif not(s[a].isalpha()or s[a].isdigit()):
                a+=1
            else:
                b-=1
        return True
        