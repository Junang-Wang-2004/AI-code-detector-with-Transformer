class C1:

    def advantageCount(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * v1
        v3 = sorted(a1)
        v4 = sorted(range(v1), key=lambda x: a2[x])
        v5 = 0
        v6 = []
        for v7 in v4:
            v8 = a2[v7]
            while v5 < v1 and v3[v5] <= v8:
                v6.append(v3[v5])
                v5 += 1
            if v5 < v1:
                v2[v7] = v3[v5]
                v5 += 1
        v9 = 0
        for v10 in range(v1):
            if v2[v10] == 0:
                v2[v10] = v6[v9]
                v9 += 1
        return v2
