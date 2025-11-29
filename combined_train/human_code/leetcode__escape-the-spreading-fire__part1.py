import collections

class C1(object):

    def maximumMinutes(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2, v3, v4, v5 = list(range(4))
        v6 = 10 ** 9

        def bfs(a1):
            v1 = collections.defaultdict(int)
            v2 = 0
            v3 = [(r, c, v3) for v4 in range(len(a1)) for v5 in range(len(a1[0])) if a1[v4][v5] == v3]
            v3.append((0, 0, v5))
            while v3:
                v6 = []
                for v4, v5, v7 in v3:
                    for v8, v9 in v1:
                        v10, v11 = (v4 + v8, v5 + v9)
                        if not (0 <= v10 < len(a1) and 0 <= v11 < len(a1[0]) and (a1[v10][v11] != v4) and (v7 == v3 and a1[v10][v11] != v3 or (v7 == v5 and (a1[v10][v11] == v2 or (a1[v10][v11] == v3 and (v10, v11) == (len(a1) - 1, len(a1[0]) - 1) and (v2 + 1 == v1[v3, v10, v11])))))):
                            continue
                        if a1[v10][v11] != v3:
                            a1[v10][v11] = v7
                        if (v10, v11) in ((len(a1) - 1, len(a1[0]) - 1), (len(a1) - 1, len(a1[0]) - 2), (len(a1) - 2, len(a1[0]) - 1)):
                            v1[v7, v10, v11] = v2 + 1
                        v6.append((v10, v11, v7))
                v3 = v6
                v2 += 1
            return v1
        v7 = bfs(a1)
        if not v7[v5, len(a1) - 1, len(a1[0]) - 1]:
            return -1
        if not v7[v3, len(a1) - 1, len(a1[0]) - 1]:
            return v6
        v8 = v7[v3, len(a1) - 1, len(a1[0]) - 1] - v7[v5, len(a1) - 1, len(a1[0]) - 1]
        return v8 if v8 + 2 in (v7[v3, len(a1) - 1, len(a1[0]) - 2] - v7[v5, len(a1) - 1, len(a1[0]) - 2], v7[v3, len(a1) - 2, len(a1[0]) - 1] - v7[v5, len(a1) - 2, len(a1[0]) - 1]) else v8 - 1
