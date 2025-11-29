def f1(a1, a2):

    def iter_dfs(a1, a2):
        v1 = [(1, (a1, a2))]
        while v1:
            v2, v3 = v1.pop()
            if v2 == 1:
                a1, a2 = v3
                index[a1] = index_counter[0]
                lowlinks[a1] = index_counter[0]
                index_counter[0] += 1
                v6 = [0]
                v7 = [False]
                v1.append((4, (a1, a2, v6, v7)))
                for v8 in reversed(a1[a1]):
                    if v8 == a2:
                        continue
                    v1.append((2, (v8, a1, v6, v7)))
            elif v2 == 2:
                v8, a1, v6, v7 = v3
                if index[v8] == -1:
                    v6[0] += 1
                    v1.append((3, (v8, a1, v7)))
                    v1.append((1, (v8, a1)))
                else:
                    lowlinks[a1] = min(lowlinks[a1], index[v8])
            elif v2 == 3:
                v8, a1, v7 = v3
                if lowlinks[v8] >= index[a1]:
                    v7[0] = True
                lowlinks[a1] = min(lowlinks[a1], lowlinks[v8])
            elif v2 == 4:
                a1, a2, v6, v7 = v3
                if a2 != -1 and v7[0] or (a2 == -1 and v6[0] >= 2):
                    cutpoints.append(a1)
    v1, v2, v3 = ([0], [-1] * len(a1), [0] * len(a1))
    v4 = []
    iter_dfs(a2, -1)
    return v4

class C1(object):

    def minDays(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def floodfill(a1, a2, a3, a4):
            v1 = [(a2, a3)]
            a4[a2][a3] = 1
            while v1:
                a2, a3 = v1.pop()
                for v4, v5 in v1:
                    v6, v7 = (a2 + v4, a3 + v5)
                    if not (0 <= v6 < R and 0 <= v7 < C and a1[v6][v7] and (not a4[v6][v7])):
                        continue
                    a4[v6][v7] = 1
                    v1.append((v6, v7))

        def count_islands(a1):
            v1 = [[0] * C for v2 in range(R)]
            v3 = 0
            for v4 in range(R):
                for v5 in range(C):
                    if a1[v4][v5] == 0 or v1[v4][v5]:
                        continue
                    v3 += 1
                    floodfill(a1, v4, v5, v1)
            return v3
        v2, v3 = (len(a1), len(a1[0]))
        if count_islands(a1) != 1:
            return 0
        v4 = [[] for v5 in range(v2 * v3)]
        v6, v7 = (0, -1)
        for v8 in range(v2):
            for v9 in range(v3):
                if a1[v8][v9] == 0:
                    continue
                v6 += 1
                if v7 == -1:
                    v7 = v8 * v3 + v9
                for v10, v11 in v1:
                    v12, v13 = (v8 + v10, v9 + v11)
                    if 0 <= v12 < v2 and 0 <= v13 < v3 and (a1[v12][v13] == a1[v8][v9]):
                        v4[v8 * v3 + v9].append(v12 * v3 + v13)
        return 1 if v6 == 1 or f1(v4, v7) else 2
