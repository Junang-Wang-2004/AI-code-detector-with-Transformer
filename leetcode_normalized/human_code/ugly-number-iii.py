class C1(object):

    def nthUglyNumber(self, a1, a2, a3, a4):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1

        def lcm(a1, a2):
            return a1 // gcd(a1, a2) * a2

        def count(a1, a2, a3, a4, a5, a6, a7, a8):
            return a1 // a2 + a1 // a3 + a1 // a4 - (a1 // a5 + a1 // a6 + a1 // a7) + a1 // a8
        v1, v2, v3 = (lcm(a2, a3), lcm(a3, a4), lcm(a4, a2))
        v4 = lcm(v1, v2)
        v5, v6 = (1, 2 * 10 ** 9)
        while v5 <= v6:
            v7 = v5 + (v6 - v5) // 2
            if count(v7, a2, a3, a4, v1, v2, v3, v4) >= a1:
                v6 = v7 - 1
            else:
                v5 = v7 + 1
        return v5
