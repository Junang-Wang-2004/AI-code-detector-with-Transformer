class C1(object):

    def maxMoves(self, a1, a2, a3):
        """
        """
        v1 = 50
        v2 = ((1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1))
        v3 = float('inf')
        v4 = float('-inf')

        def popcount(a1):
            return bin(a1)[2:].count('1')

        def bfs(a1, a2):
            v1 = [[v3] * v1 for v2 in range(v1)]
            v1[a1][a2] = 0
            v3 = [(a1, a2)]
            while v3:
                v4 = []
                for a1, a2 in v3:
                    for v7, v8 in v2:
                        v9, v10 = (a1 + v7, a2 + v8)
                        if not (0 <= v9 < v1 and 0 <= v10 < v1 and (v1[v9][v10] == v3)):
                            continue
                        v1[v9][v10] = v1[a1][a2] + 1
                        v4.append((v9, v10))
                v3 = v4
            return v1
        v5 = len(a3)
        a3.append([a1, a2])
        v6 = [[0] * (v5 + 1) for v7 in range(v5 + 1)]
        for v8, (v9, v10) in enumerate(a3):
            v11 = bfs(v9, v10)
            for v12 in range(v8 + 1, v5 + 1):
                v6[v12][v8] = v6[v8][v12] = v11[a3[v12][0]][a3[v12][1]]
        v13 = [[v3 if popcount(mask) & 1 else v4] * v5 for v14 in range(1 << v5)]
        v13[-1] = [0] * v5
        for v14 in reversed(range(1, 1 << v5)):
            v15 = (max, min)[popcount(v14) & 1 ^ 1]
            for v8 in range(v5):
                if v14 & 1 << v8 == 0:
                    continue
                for v12 in range(v5):
                    if v12 == v8 or v14 & 1 << v12 == 0:
                        continue
                    v13[v14 ^ 1 << v8][v12] = v15(v13[v14 ^ 1 << v8][v12], v13[v14][v8] + v6[v8][v12])
        return max((v13[1 << v8][v8] + v6[v8][v5] for v8 in range(v5)))
