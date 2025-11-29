class Solution:
    def decodeString(self, s):
        stk = []
        multiplier = 0
        result = ""
        for char in s:
            if char.isdigit():
                multiplier = multiplier * 10 + int(char)
            elif char == '[':
                stk.append(result)
                stk.append(multiplier)
                result = ""
                multiplier = 0
            elif char == ']':
                prev_mult = stk.pop()
                prev_result = stk.pop()
                result = prev_result + result * prev_mult
            else:
                result += char
        return result
