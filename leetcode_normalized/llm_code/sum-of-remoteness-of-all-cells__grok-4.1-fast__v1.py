class C1:

    def sumRemoteness(self, a1):
        if not a1 or not a1[0]:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = sum((a1[i][j] for v4 in range(v1) for v5 in range(v2) if a1[v4][v5] != -1))
        v6 = [[False] * v2 for v7 in range(v1)]
        v8 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def explore(a1, a2):
            v1 = [(a1, a2)]
            v6[a1][a2] = True
            v2 = a1[a1][a2]
            v3 = 1
            while v1:
                v4, v5 = v1.pop()
                for v6, v7 in v8:
                    v8, v9 = (v4 + v6, v5 + v7)
                    if 0 <= v8 < v1 and 0 <= v9 < v2 and (a1[v8][v9] != -1) and (not v6[v8][v9]):
                        v6[v8][v9] = True
                        v2 += a1[v8][v9]
                        v3 += 1
                        v1.append((v8, v9))
            return (v2, v3)
        v9 = 0
        for v4 in range(v1):
            for v5 in range(v2):
                if a1[v4][v5] != -1 and (not v6[v4][v5]):
                    v10, v11 = explore(v4, v5)
                    v9 += (v3 - v10) * v11
        return v9
