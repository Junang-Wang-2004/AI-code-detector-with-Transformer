class C1(object):

    def maxTaxiEarnings(self, a1, a2):
        v1 = [0] * (a1 + 1)
        v2 = [[] for v3 in range(a1 + 1)]
        for v4, v5, v6 in a2:
            v2[v4].append((v5, v6))
        for v7 in range(1, a1 + 1):
            v1[v7] = max(v1[v7], v1[v7 - 1])
            for v8, v9 in v2[v7]:
                v10 = v8 - v7 + v9
                v1[v8] = max(v1[v8], v1[v7] + v10)
        return v1[a1]
