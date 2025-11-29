class C1:

    def minimumSplits(self, a1):

        def gcd(a1, a2):
            while a1 and a2:
                a1, a2 = (a2, a1 % a2)
            return a1 or a2
        v1, v2 = (0, 0)
        for v3 in a1:
            v4 = gcd(v2, v3)
            if v4 == 1:
                v1 += 1
                v2 = v3
            else:
                v2 = v4
        return v1 + 1
