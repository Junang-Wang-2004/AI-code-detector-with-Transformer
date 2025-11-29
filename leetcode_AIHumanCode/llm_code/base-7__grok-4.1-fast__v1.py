class Solution:
    def convertToBase7(self, n):
        if n == 0:
            return '0'
        sign = '-' if n < 0 else ''
        val = abs(n)
        digits = []
        while val > 0:
            digits.append(str(val % 7))
            val //= 7
        return sign + ''.join(reversed(digits))
