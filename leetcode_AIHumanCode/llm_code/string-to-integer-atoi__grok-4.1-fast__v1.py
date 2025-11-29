class Solution(object):
    def myAtoi(self, s):
        if not s:
            return 0
        pos = 0
        n = len(s)
        while pos < n and s[pos].isspace():
            pos += 1
        if pos == n:
            return 0
        sign = 1
        if s[pos] == '+':
            pos += 1
        elif s[pos] == '-':
            sign = -1
            pos += 1
        num = 0
        BOUND = 2147483647
        LOWER = -2147483648
        DIGIT_BOUND = BOUND // 10
        LAST_DIGIT = BOUND % 10
        while pos < n and s[pos].isdigit():
            d = ord(s[pos]) - ord('0')
            if num > DIGIT_BOUND or (num == DIGIT_BOUND and d > LAST_DIGIT):
                return BOUND if sign == 1 else LOWER
            num = num * 10 + d
            pos += 1
        return sign * num
