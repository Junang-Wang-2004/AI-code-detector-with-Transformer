class C1(object):

    def maxGcdSum(self, a1, a2):

        def gcd(a1, a2):
            return a1 if a2 == 0 else gcd(a2, a1 % a2)
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = 0
        v5 = {}
        for v6 in range(v1):
            v7 = {}
            for v8, v9 in v5.items():
                v10 = gcd(v8, a1[v6])
                if v10 not in v7 or v9 < v7[v10]:
                    v7[v10] = v9
            v10 = a1[v6]
            v9 = v6
            if v10 not in v7 or v9 < v7[v10]:
                v7[v10] = v9
            v5 = v7
            v11 = v6 - a2 + 1
            for v12, v9 in v5.items():
                if v9 <= v11:
                    v13 = v2[v6 + 1] - v2[v9]
                    v4 = max(v4, v12 * v13)
        return v4
