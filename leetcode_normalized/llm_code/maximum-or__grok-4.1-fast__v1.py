class C1:

    def maximumOr(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] | a1[v3]
        v4 = [0] * (v1 + 1)
        for v3 in range(v1 - 1, -1, -1):
            v4[v3] = a1[v3] | v4[v3 + 1]
        v5 = 0
        for v3 in range(v1):
            v6 = v2[v3] | a1[v3] << a2 | v4[v3 + 1]
            if v6 > v5:
                v5 = v6
        return v5
