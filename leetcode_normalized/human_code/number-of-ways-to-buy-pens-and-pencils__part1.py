class C1(object):

    def waysToBuyPensPencils(self, a1, a2, a3):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2

        def arithmetic_progression_sum(a1, a2, a3):
            return (a1 + (a1 + (a3 - 1) * a2)) * a3 // 2
        if a2 < a3:
            a2, a3 = (a3, a2)
        v3 = a2 * a3 // gcd(a2, a3)
        v4 = 0
        v5 = v3 // a3
        for v6 in range(min(a1 // a2 + 1, v3 // a2)):
            v7 = (a1 - v6 * a2) // a3 + 1
            v8 = ceil_divide(v7, v5)
            v4 += arithmetic_progression_sum(v7, -v5, v8)
        return v4
