from collections import deque

class C1:

    def pacificAtlantic(self, a1):
        if not a1 or not a1[0]:
            return []
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [[False] * v2 for v4 in range(v1)]
        v5 = [[False] * v2 for v4 in range(v1)]
        v6 = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def flood(a1, a2):
            v1 = deque(a2)
            for v2, v3 in a2:
                a1[v2][v3] = True
            while v1:
                v2, v3 = v1.popleft()
                v4 = a1[v2][v3]
                for v5, v6 in v6:
                    v7, v8 = (v2 + v5, v3 + v6)
                    if 0 <= v7 < v1 and 0 <= v8 < v2 and (not a1[v7][v8]) and (a1[v7][v8] >= v4):
                        a1[v7][v8] = True
                        v1.append((v7, v8))
        v7 = [(i, 0) for v8 in range(v1)] + [(0, j) for v9 in range(1, v2)]
        v10 = [(v8, v2 - 1) for v8 in range(v1)] + [(v1 - 1, v9) for v9 in range(v2 - 1)]
        flood(v3, v7)
        flood(v5, v10)
        v11 = []
        for v8 in range(v1):
            for v9 in range(v2):
                if v3[v8][v9] and v5[v8][v9]:
                    v11.append([v8, v9])
        return v11
