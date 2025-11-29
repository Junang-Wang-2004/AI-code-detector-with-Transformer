class Solution:
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        def lcm(a, b):
            g = gcd(a, b)
            return a // g * b

        def required_size(d, need):
            if need == 0:
                return 0
            period = d - 1
            groups = need // period
            remainder = need % period
            if remainder == 0:
                return groups * d - 1
            return groups * d + remainder

        common_multiple = lcm(divisor1, divisor2)
        size1 = required_size(divisor1, uniqueCnt1)
        size2 = required_size(divisor2, uniqueCnt2)
        size3 = required_size(common_multiple, uniqueCnt1 + uniqueCnt2)
        return max(size1, size2, size3)
