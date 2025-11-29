class C1:

    def findPermutation(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return []
        v2 = v1 - 1
        v3 = 1 << v2
        v4 = v3 - 1
        v5 = float('inf')
        v6 = [[v5] * v2 for v7 in range(v3)]
        v8 = [[-1] * v2 for v7 in range(v3)]
        for v9 in range(v2):
            v10 = 1 << v9
            v6[v10][v9] = abs(v9 + 1 - a1[0])
            v8[v10][v9] = -1
        for v10 in range(v3):
            for v9 in range(v2):
                if v10 & 1 << v9 == 0:
                    continue
                for v11 in range(v2):
                    if v11 == v9 or v10 & 1 << v11 == 0:
                        continue
                    v12 = v10 ^ 1 << v9
                    v13 = abs(v9 + 1 - a1[v11 + 1])
                    v14 = v6[v12][v11] + v13
                    if v14 < v6[v10][v9]:
                        v6[v10][v9] = v14
                        v8[v10][v9] = v11
        v15 = v5
        v16 = -1
        for v9 in range(v2):
            v17 = v6[v4][v9] + abs(a1[v9 + 1] - 0)
            if v17 < v15 or (v17 == v15 and v9 < v16):
                v15 = v17
                v16 = v9
        v18 = []
        v10 = v4
        v9 = v16
        while v9 != -1:
            v18.append(v9 + 1)
            v11 = v8[v10][v9]
            v10 ^= 1 << v9
            v9 = v11
        v18.reverse()
        return [0] + v18
