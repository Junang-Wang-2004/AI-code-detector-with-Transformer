from collections import deque

class C1:

    def shortestDistance(self, a1):
        if not a1 or not a1[0]:
            return -1
        v1, v2 = (len(a1), len(a1[0]))
        v3 = sum((1 for v4 in range(v1) for v5 in range(v2) if a1[v4][v5] == 1))
        v6 = [[0] * v2 for v7 in range(v1)]
        v8 = [[0] * v2 for v7 in range(v1)]

        def explore(a1, a2):
            v1 = [[False] * v2 for v7 in range(v1)]
            v2 = deque([(a1, a2, 0)])
            v1[a1][a2] = True
            while v2:
                v3, v4, v5 = v2.popleft()
                if a1[v3][v4] == 0:
                    v6[v3][v4] += v5
                    v8[v3][v4] += 1
                for v6, v7 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    v8, v9 = (v3 + v6, v4 + v7)
                    if 0 <= v8 < v1 and 0 <= v9 < v2 and (a1[v8][v9] == 0) and (not v1[v8][v9]):
                        v1[v8][v9] = True
                        v2.append((v8, v9, v5 + 1))
        for v4 in range(v1):
            for v5 in range(v2):
                if a1[v4][v5] == 1:
                    explore(v4, v5)
        v9 = float('inf')
        for v4 in range(v1):
            for v5 in range(v2):
                if a1[v4][v5] == 0 and v8[v4][v5] == v3:
                    v9 = min(v9, v6[v4][v5])
        return v9 if v9 != float('inf') else -1
