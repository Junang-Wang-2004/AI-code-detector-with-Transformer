class C1:

    def largestIsland(self, a1):
        if not a1 or not a1[0]:
            return 1
        v1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        v2, v3 = (len(a1), len(a1[0]))
        v4 = {}

        def comp_size(a1, a2, a3):
            v1 = [(a1, a2)]
            v2 = 0
            a1[a1][a2] = a3
            v2 += 1
            while v1:
                v3, v4 = v1.pop()
                for v5, v6 in v1:
                    v7, v8 = (v3 + v5, v4 + v6)
                    if 0 <= v7 < v2 and 0 <= v8 < v3 and (a1[v7][v8] == 1):
                        a1[v7][v8] = a3
                        v2 += 1
                        v1.append((v7, v8))
            return v2
        v5 = 2
        for v6 in range(v2):
            for v7 in range(v3):
                if a1[v6][v7] == 1:
                    v4[v5] = comp_size(v6, v7, v5)
                    v5 += 1
        v8 = max(v4.values()) if v4 else 0
        for v6 in range(v2):
            for v7 in range(v3):
                if a1[v6][v7] == 0:
                    v9 = set()
                    for v10, v11 in v1:
                        v12, v13 = (v6 + v10, v7 + v11)
                        if 0 <= v12 < v2 and 0 <= v13 < v3 and (a1[v12][v13] >= 2):
                            v9.add(a1[v12][v13])
                    v14 = 1 + sum((v4.get(k, 0) for v15 in v9))
                    v8 = max(v8, v14)
        return v8
