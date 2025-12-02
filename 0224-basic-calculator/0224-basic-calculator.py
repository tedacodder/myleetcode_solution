class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1   # +1 or -1
        result = 0

        i = 0
        while i < len(s):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch in "+-":
                result += sign * num
                num = 0
                sign = 1 if ch == "+" else -1

            elif ch == "(":
                # push the result and the sign
                stack.append(result)
                stack.append(sign)
                # reset for inside parentheses
                result = 0
                sign = 1

            elif ch == ")":
                # complete the current number first
                result += sign * num
                num = 0

                # pop the sign
                result *= stack.pop()
                # add previous result
                result += stack.pop()

            i += 1

        return result + sign * num
