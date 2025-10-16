class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        prev = 0

        
        for ch in reversed(s):
            value = dic[ch]
            if value < prev:
                ans -= value   
            else:
                ans += value   
            prev = value

        return ans
