class Solution:
    def minimumTime(self, dist, rates):
        def gcd(x, y):
            return x if y == 0 else gcd(y, x % y)

        def lcm(a, b):
            g = gcd(a, b)
            return a // g * b

        def need_time(p, dd):
            if dd == 0:
                return 0
            m = p - 1
            q = (dd + m - 1) // m
            k = q - 1
            extra = dd - k * m
            return k * p + extra

        r0, r1 = rates
        d0, d1 = dist
        lc = lcm(r0, r1)
        return max(need_time(r0, d0), need_time(r1, d1), need_time(lc, d0 + d1))
