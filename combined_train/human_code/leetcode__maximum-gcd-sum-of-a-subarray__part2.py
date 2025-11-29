class C1(object):

    def maxGcdSum(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = [0] * (len(a1) + 1)
        for v2, v3 in enumerate(a1):
            v1[v2 + 1] = v1[v2] + v3
        v4 = 0
        v5 = []
        for v6, v3 in enumerate(a1):
            v5.append((v6, v3))
            v7 = []
            for v8, v9 in v5:
                v10 = gcd(v9, v3)
                if not v7 or v7[-1][1] != v10:
                    v7.append((v8, v10))
            v5 = v7
            for v8, v9 in v5:
                if v6 - v8 + 1 < a2:
                    break
                v4 = max(v4, (v1[v6 + 1] - v1[v8]) * v9)
        return v4
