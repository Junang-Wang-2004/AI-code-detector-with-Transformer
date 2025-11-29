class Solution:
    def divide(self, dividend, divisor):
        sign = 1 if (dividend > 0) == (divisor > 0) else -1
        a, b = abs(dividend), abs(divisor)
        q = 0
        for k in range(31, -1, -1):
            if a >= b << k:
                a -= b << k
                q |= 1 << k
        res = sign * q
        lo = -(1 << 31)
        hi = (1 << 31) - 1
        return max(lo, min(res, hi))
