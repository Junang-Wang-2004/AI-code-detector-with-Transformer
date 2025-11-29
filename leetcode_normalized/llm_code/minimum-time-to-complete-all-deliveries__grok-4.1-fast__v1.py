class C1:

    def minimumTime(self, a1, a2):

        def gcd(a1, a2):
            return a1 if a2 == 0 else gcd(a2, a1 % a2)

        def lcm(a1, a2):
            v1 = gcd(a1, a2)
            return a1 // v1 * a2

        def need_time(a1, a2):
            if a2 == 0:
                return 0
            v1 = a1 - 1
            v2 = (a2 + v1 - 1) // v1
            v3 = v2 - 1
            v4 = a2 - v3 * v1
            return v3 * a1 + v4
        v1, v2 = a2
        v3, v4 = a1
        v5 = lcm(v1, v2)
        return max(need_time(v1, v3), need_time(v2, v4), need_time(v5, v3 + v4))
