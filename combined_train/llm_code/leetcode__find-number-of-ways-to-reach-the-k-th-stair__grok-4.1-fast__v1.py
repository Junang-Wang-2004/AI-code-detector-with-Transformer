class C1:

    def waysToReachStair(self, a1):

        def binom(a1, a2):
            if a2 < 0 or a2 > a1:
                return 0
            if a2 > a1 - a2:
                a2 = a1 - a2
            v2 = 1
            for v3 in range(a2):
                v2 = v2 * (a1 - v3) // (v3 + 1)
            return v2
        v1 = 0
        v2 = 0
        while True:
            v3 = (1 << v2) - a1
            if v3 > v2 + 1:
                break
            v1 += binom(v2 + 1, v3)
            v2 += 1
        return v1
