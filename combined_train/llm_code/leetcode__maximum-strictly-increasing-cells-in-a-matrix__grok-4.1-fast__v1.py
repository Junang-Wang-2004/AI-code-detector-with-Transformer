class C1(object):

    def maxIncreasingCells(self, a1):
        if not a1 or not a1[0]:
            return 0
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = []
        for v4 in range(v1):
            for v5 in range(v2):
                v3.append((a1[v4][v5], v4, v5))
        v3.sort()
        v6 = [0] * v1
        v7 = [0] * v2
        v8 = 0
        v9 = 0
        v10 = len(v3)
        while v9 < v10:
            v11 = v3[v9][0]
            v12 = []
            while v9 < v10 and v3[v9][0] == v11:
                v13, v14, v15 = v3[v9]
                v16 = max(v6[v14], v7[v15]) + 1
                v12.append((v14, v15, v16))
                v8 = max(v8, v16)
                v9 += 1
            for v14, v15, v16 in v12:
                v6[v14] = max(v6[v14], v16)
                v7[v15] = max(v7[v15], v16)
        return v8
