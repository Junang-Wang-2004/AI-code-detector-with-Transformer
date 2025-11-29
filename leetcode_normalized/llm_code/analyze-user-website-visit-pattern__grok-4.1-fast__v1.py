class C1:

    def mostVisitedPattern(self, a1, a2, a3):
        v1 = {}
        v2 = len(a1)
        for v3 in range(v2):
            v4 = a1[v3]
            if v4 not in v1:
                v1[v4] = []
            v1[v4].append((a2[v3], a3[v3]))
        v5 = {}
        for v6 in v1.values():
            v6.sort(key=lambda x: x[0])
            v7 = [site for v8, v9 in v6]
            v10 = len(v7)
            v11 = set()
            for v3 in range(v10):
                for v12 in range(v3 + 1, v10):
                    for v13 in range(v12 + 1, v10):
                        v14 = (v7[v3], v7[v12], v7[v13])
                        v11.add(v14)
            for v14 in v11:
                v5[v14] = v5.get(v14, 0) + 1
        v15 = -1
        v16 = None
        for v14, v17 in v5.items():
            if v17 > v15 or (v17 == v15 and (v16 is None or v14 < v16)):
                v15 = v17
                v16 = v14
        return list(v16)
