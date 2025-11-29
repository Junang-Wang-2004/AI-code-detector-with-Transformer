class C1:

    def gameOfLife(self, a1):
        if not a1:
            return
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for v4 in range(v1):
            for v5 in range(v2):
                v6 = sum((a1[v4 + dx][v5 + dy] & 1 for v7, v8 in v3 if 0 <= v4 + v7 < v1 and 0 <= v5 + v8 < v2))
                v9 = a1[v4][v5] & 1
                if v9 and 2 <= v6 <= 3 or (not v9 and v6 == 3):
                    a1[v4][v5] |= 2
        for v4 in range(v1):
            for v5 in range(v2):
                a1[v4][v5] >>= 1
