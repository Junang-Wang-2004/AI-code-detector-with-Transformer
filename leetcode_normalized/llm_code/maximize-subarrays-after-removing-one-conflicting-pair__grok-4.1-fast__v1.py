class C1:

    def maxSubarrays(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v5 = v3 - 1
            v6 = v4 - 1
            if v5 > v6:
                v5, v6 = (v6, v5)
            v1[v6].append(v5)
        v7 = 0
        v8 = -1
        for v9 in range(a1):
            for v10 in v1[v9]:
                if v10 > v8:
                    v8 = v10
            v7 += v9 - v8
        return v7
