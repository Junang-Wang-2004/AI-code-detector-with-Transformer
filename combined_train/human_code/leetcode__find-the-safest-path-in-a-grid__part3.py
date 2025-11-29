import heapq

class C1(object):

    def maximumSafenessFactor(self, a1):
        """
        """
        v1 = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def bfs():
            v1 = [[0 if a1[r][c] == 1 else -1 for v2 in range(len(a1[0]))] for v3 in range(len(a1))]
            v4 = [(v3, v2) for v3 in range(len(a1)) for v2 in range(len(a1[0])) if a1[v3][v2]]
            v5 = 0
            while v4:
                v6 = []
                for v3, v2 in v4:
                    for v7, v8 in v1:
                        v9, v10 = (v3 + v7, v2 + v8)
                        if not (0 <= v9 < len(v1) and 0 <= v10 < len(v1[0]) and (v1[v9][v10] == -1)):
                            continue
                        v1[v9][v10] = v5 + 1
                        v6.append((v9, v10))
                v4 = v6
                v5 += 1
            return v1

        def check(a1):
            v1 = [[False] * len(dist[0]) for v2 in range(len(dist))]
            v3 = [(0, 0)]
            v1[0][0] = True
            while v3:
                v4 = []
                for v5, v6 in v3:
                    for v7, v8 in v1:
                        v9, v10 = (v5 + v7, v6 + v8)
                        if not (0 <= v9 < len(dist) and 0 <= v10 < len(dist[0]) and (dist[v9][v10] >= a1) and (not v1[v9][v10])):
                            continue
                        v1[v9][v10] = True
                        v4.append((v9, v10))
                v3 = v4
            return v1[-1][-1]
        v2 = bfs()
        v3, v4 = (0, v2[0][0])
        while v3 <= v4:
            v5 = v3 + (v4 - v3) // 2
            if not check(v5):
                v4 = v5 - 1
            else:
                v3 = v5 + 1
        return v4
