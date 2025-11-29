class C1(object):

    def shortestDistance(self, a1):
        """
        """

        def bfs(a1, a2, a3, a4, a5):
            v1, v2, v3 = (0, len(a1), len(a1[0]))
            v4 = [[False for v5 in range(v3)] for v5 in range(v2)]
            v6 = [(a4, a5)]
            v4[a4][a5] = True
            while v6:
                v1 += 1
                v7 = []
                for v8, v9 in v6:
                    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        v10, v11 = (v8 + dir[0], v9 + dir[1])
                        if 0 <= v10 < v2 and 0 <= v11 < v3 and (a1[v10][v11] == 0) and (not v4[v10][v11]):
                            a3[v10][v11] += 1
                            a2[v10][v11] += v1
                            v7.append((v10, v11))
                            v4[v10][v11] = True
                v6 = v7
        v1, v2, v3 = (len(a1), len(a1[0]), 0)
        v4 = [[0 for v5 in range(v2)] for v5 in range(v1)]
        v6 = [[0 for v5 in range(v2)] for v5 in range(v1)]
        for v7 in range(v1):
            for v8 in range(v2):
                if a1[v7][v8] == 1:
                    v3 += 1
                    bfs(a1, v4, v6, v7, v8)
        v9 = float('inf')
        for v7 in range(v1):
            for v8 in range(v2):
                if v4[v7][v8] < v9 and v6[v7][v8] == v3:
                    v9 = v4[v7][v8]
        return v9 if v9 != float('inf') else -1
