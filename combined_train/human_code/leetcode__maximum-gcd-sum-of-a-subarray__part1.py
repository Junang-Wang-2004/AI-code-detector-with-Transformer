class C1(object):

    def maxGcdSum(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = v2 = 0
        v3 = []
        for v4, v5 in enumerate(a1):
            v3.append((v4, v5, v2))
            v2 += v5
            v6 = []
            for v7, v8, v9 in v3:
                v10 = gcd(v8, v5)
                if not v6 or v6[-1][1] != v10:
                    v6.append((v7, v10, v9))
            v3 = v6
            for v7, v8, v9 in v3:
                if v4 - v7 + 1 < a2:
                    break
                v1 = max(v1, (v2 - v9) * v8)
        return v1
