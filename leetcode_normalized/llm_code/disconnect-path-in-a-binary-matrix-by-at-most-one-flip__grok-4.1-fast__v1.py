class C1:

    def isPossibleToCutPath(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [[False] * v2 for v4 in range(v1)]
        for v5 in range(v1):
            for v6 in range(v2):
                if a1[v5][v6] == 0:
                    continue
                if v5 == 0 and v6 == 0:
                    v3[v5][v6] = True
                elif v5 > 0 and v3[v5 - 1][v6] or (v6 > 0 and v3[v5][v6 - 1]):
                    v3[v5][v6] = True
        v7 = [[False] * v2 for v4 in range(v1)]
        for v5 in range(v1 - 1, -1, -1):
            for v6 in range(v2 - 1, -1, -1):
                if a1[v5][v6] == 0:
                    continue
                if v5 == v1 - 1 and v6 == v2 - 1:
                    v7[v5][v6] = True
                elif v5 + 1 < v1 and v7[v5 + 1][v6] or (v6 + 1 < v2 and v7[v5][v6 + 1]):
                    v7[v5][v6] = True
        for v8 in range(1, v1 + v2 - 2):
            v9 = 0
            v10 = max(0, v8 - v2 + 1)
            v11 = min(v8, v1 - 1)
            for v5 in range(v10, v11 + 1):
                v6 = v8 - v5
                if v3[v5][v6] and v7[v5][v6]:
                    v9 += 1
            if v9 <= 1:
                return True
        return False
