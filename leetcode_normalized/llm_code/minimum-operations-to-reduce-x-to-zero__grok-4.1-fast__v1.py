class C1(object):

    def minOperations(self, a1, a2):
        v1 = len(a1)
        v2 = sum(a1)
        v3 = v2 - a2
        v4 = [0] * (v1 + 1)
        for v5 in range(v1):
            v4[v5 + 1] = v4[v5] + a1[v5]
        v6 = {}
        v7 = 0
        for v8 in range(v1 + 1):
            v9 = v4[v8]
            v10 = v9 - v3
            if v10 in v6:
                v7 = max(v7, v8 - v6[v10])
            if v9 not in v6:
                v6[v9] = v8
        return v1 - v7 if v7 > 0 else -1
