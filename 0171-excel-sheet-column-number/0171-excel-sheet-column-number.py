class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result=0
        for c in columnTitle:
            result=result*26+(ord(c)-64)
        return result
        