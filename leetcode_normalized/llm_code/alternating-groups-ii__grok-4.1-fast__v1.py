class C1:

    def numberOfAlternatingGroups(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * v1
        for v3 in range(v1):
            v2[v3] = 1 if a1[v3] != a1[(v3 + 1) % v1] else 0
        v4 = v2 + v2
        v5 = [0] * (2 * v1 + 1)
        for v3 in range(2 * v1):
            v5[v3 + 1] = v5[v3] + v4[v3]
        v6 = 0
        v7 = a2 - 1
        for v8 in range(v1):
            if v5[v8 + v7] - v5[v8] == v7:
                v6 += 1
        return v6
