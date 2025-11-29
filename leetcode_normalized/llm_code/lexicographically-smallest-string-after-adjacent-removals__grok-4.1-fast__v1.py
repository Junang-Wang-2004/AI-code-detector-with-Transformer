class C1:

    def lexicographicallySmallestString(self, a1):
        v1 = len(a1)
        v2 = [[False] * v1 for v3 in range(v1)]
        v4 = {1, 25}
        for v5 in range(v1 - 1):
            if abs(ord(a1[v5]) - ord(a1[v5 + 1])) in v4:
                v2[v5][v5 + 1] = True
        for v6 in range(4, v1 + 1, 2):
            for v7 in range(v1 - v6 + 1):
                v8 = v7 + v6 - 1
                if abs(ord(a1[v7]) - ord(a1[v8])) in v4 and v2[v7 + 1][v8 - 1]:
                    v2[v7][v8] = True
                for v9 in range(v7 + 1, v8, 2):
                    if v2[v7][v9] and v2[v9 + 1][v8]:
                        v2[v7][v8] = True
                        break
        v10 = [''] * (v1 + 1)
        for v11 in range(v1 - 1, -1, -1):
            v12 = a1[v11] + v10[v11 + 1]
            v13 = v11 + 1
            while v13 < v1:
                if v2[v11][v13]:
                    v12 = min(v12, v10[v13 + 1])
                v13 += 2
            v10[v11] = v12
        return v10[0]
