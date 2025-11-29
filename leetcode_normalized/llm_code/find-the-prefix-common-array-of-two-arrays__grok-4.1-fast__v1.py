class C1:

    def findThePrefixCommonArray(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        v3 = [0] * (v1 + 1)
        for v4 in range(v1):
            v2[a1[v4]] = v4
            v3[a2[v4]] = v4
        v5 = [0] * v1
        for v6 in range(1, v1 + 1):
            v7 = max(v2[v6], v3[v6])
            v5[v7] += 1
        v8 = []
        v9 = 0
        for v4 in range(v1):
            v9 += v5[v4]
            v8.append(v9)
        return v8
