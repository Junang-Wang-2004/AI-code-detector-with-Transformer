class C1:

    def countDistinct(self, a1):
        v1 = len(a1)
        v2 = sorted(range(v1), key=lambda idx: a1[idx:])
        v3 = [0] * v1
        for v4 in range(1, v1):
            v5 = v2[v4 - 1]
            v6 = v2[v4]
            v7 = 0
            while v5 + v7 < v1 and v6 + v7 < v1 and (a1[v5 + v7] == a1[v6 + v7]):
                v7 += 1
            v3[v4] = v7
        v8 = 0
        for v9 in range(v1):
            v8 += v1 - v2[v9] - v3[v9]
        return v8
