class C1:

    def maxNonOverlapping(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(1, v1 + 1):
            v2[v3] = v2[v3 - 1] + a1[v3 - 1]
        v4 = {0: 0}
        v5 = 0
        v6 = -1
        for v7 in range(1, v1 + 1):
            v8 = v2[v7]
            v9 = v8 - a2
            if v9 in v4 and v4[v9] > v6:
                v6 = v7 - 1
                v5 += 1
            v4[v8] = v7
        return v5
