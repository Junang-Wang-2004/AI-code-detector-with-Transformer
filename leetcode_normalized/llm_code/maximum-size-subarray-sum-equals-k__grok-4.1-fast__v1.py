class C1:

    def maxSubArrayLen(self, a1, a2):
        v1 = {0: -1}
        v2 = 0
        v3 = 0
        for v4, v5 in enumerate(a1):
            v2 += v5
            v6 = v2 - a2
            if v6 in v1:
                v3 = max(v3, v4 - v1[v6])
            if v2 not in v1:
                v1[v2] = v4
        return v3
