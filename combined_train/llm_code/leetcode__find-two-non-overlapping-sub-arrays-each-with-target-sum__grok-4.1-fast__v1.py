class C1(object):

    def minSumOfLengths(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = {}
        v5 = [float('inf')] * v1
        for v3 in range(v1):
            v6 = v2[v3 + 1]
            if v6 - a2 in v4:
                v7 = v4[v6 - a2]
                v5[v3] = v3 - v7
            v4[v6] = v3
        v8 = [float('inf')] * (v1 + 1)
        for v9 in range(1, v1 + 1):
            v8[v9] = min(v8[v9 - 1], v5[v9 - 1])
        v10 = float('inf')
        for v3 in range(v1):
            if v5[v3] < float('inf'):
                v11 = v3 - v5[v3] + 1
                if v11 > 0:
                    v10 = min(v10, v8[v11] + v5[v3])
        return v10 if v10 < float('inf') else -1
