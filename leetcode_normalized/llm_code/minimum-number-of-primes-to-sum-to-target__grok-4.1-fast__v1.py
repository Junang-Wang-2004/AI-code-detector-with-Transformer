class C1(object):

    def minNumberOfPrimes(self, a1, a2):
        if a1 == 0:
            return 0
        v1 = [True] * (a1 + 1)
        v1[0] = v1[1] = False
        for v2 in range(2, int(a1 ** 0.5) + 1):
            if v1[v2]:
                for v3 in range(v2 * v2, a1 + 1, v2):
                    v1[v3] = False
        v4 = [v2 for v2 in range(2, a1 + 1) if v1[v2]][:a2]
        v5 = float('inf')
        v6 = [v5] * (a1 + 1)
        v6[0] = 0
        for v7 in v4:
            for v8 in range(v7, a1 + 1):
                v6[v8] = min(v6[v8], v6[v8 - v7] + 1)
        return v6[a1] if v6[a1] != v5 else -1
