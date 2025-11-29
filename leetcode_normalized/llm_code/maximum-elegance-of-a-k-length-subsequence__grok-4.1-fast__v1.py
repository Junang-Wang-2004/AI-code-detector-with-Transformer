class C1:

    def findMaximumElegance(self, a1, a2):
        v1 = sorted(a1, key=lambda x: -x[0])
        v2 = len(v1)
        v3 = 0
        v4 = set()
        v5 = []
        for v6 in range(min(a2, v2)):
            v7, v8 = v1[v6]
            v3 += v7
            if v8 in v4:
                v5.append(v7)
            v4.add(v8)
        v9 = len(v4)
        v10 = v3 + v9 * v9
        v11 = {}
        for v6 in range(a2, v2):
            v7, v8 = v1[v6]
            if v8 not in v4:
                v11[v8] = max(v11.get(v8, 0), v7)
        v12 = sorted(v11.values(), reverse=True)
        v5.sort()
        v13 = v3
        v14 = min(len(v5), len(v12))
        for v6 in range(v14):
            v13 += v12[v6] - v5[v6]
            v15 = v9 + v6 + 1
            v10 = max(v10, v13 + v15 * v15)
        return v10
