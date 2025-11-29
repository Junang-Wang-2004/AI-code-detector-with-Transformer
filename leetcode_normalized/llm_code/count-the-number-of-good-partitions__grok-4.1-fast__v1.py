class C1:

    def numberOfGoodPartitions(self, a1):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = {}
        for v4, v5 in enumerate(a1):
            v3[v5] = v4
        v6 = 0
        v7 = 0
        while v7 < v2:
            v6 += 1
            v8 = v3[a1[v7]]
            v9 = v7
            while v9 <= v8:
                v8 = max(v8, v3[a1[v9]])
                v9 += 1
            v7 = v8 + 1
        v10 = max(0, v6 - 1)
        return pow(2, v10, v1)
