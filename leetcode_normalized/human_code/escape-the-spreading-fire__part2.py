class C1(object):

    def maximumMinutes(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2, v3, v4 = list(range(1, 4))
        v5 = 10 ** 9

        def bfs(a1):
            v1 = {v2: [[v5] * len(a1[0]) for v2 in range(len(a1))], v4: [[v5] * len(a1[0]) for v2 in range(len(a1))]}
            v3 = 0
            v4 = [(r, c, v2) for v5 in range(len(a1)) for v6 in range(len(a1[0])) if a1[v5][v6] == v2]
            v4.append((0, 0, v4))
            for v5, v6, v7 in v4:
                v1[v7][v5][v6] = v3
            while v4:
                v8 = []
                for v5, v6, v7 in v4:
                    for v9, v10 in v1:
                        v11, v12 = (v5 + v9, v6 + v10)
                        if not (0 <= v11 < len(a1) and 0 <= v12 < len(a1[0]) and (a1[v11][v12] != v3) and (v1[v7][v11][v12] == v5) and (v7 == v2 or v3 + 1 < v1[v2][v11][v12] or (v3 + 1 == v1[v2][v11][v12] and (v11, v12) == (len(a1) - 1, len(a1[0]) - 1)))):
                            continue
                        v1[v7][v11][v12] = v3 + 1
                        v8.append((v11, v12, v7))
                v4 = v8
                v3 += 1
            return v1
        v6 = bfs(a1)
        if v6[v4][-1][-1] == v5:
            return -1
        if v6[v2][-1][-1] == v5:
            return v5
        v7 = v6[v2][-1][-1] - v6[v4][-1][-1]
        return v7 if v7 + 2 in (v6[v2][-1][-2] - v6[v4][-1][-2], v6[v2][-2][-1] - v6[v4][-2][-1]) else v7 - 1
