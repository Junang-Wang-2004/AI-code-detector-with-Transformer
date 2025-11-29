from collections import deque

class C1:

    def numEnclaves(self, a1):
        if not a1 or not a1[0]:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = deque()
        for v4 in range(v1):
            if a1[v4][0]:
                v3.append((v4, 0))
                a1[v4][0] = 0
            if a1[v4][v2 - 1]:
                v3.append((v4, v2 - 1))
                a1[v4][v2 - 1] = 0
        for v5 in range(1, v2 - 1):
            if a1[0][v5]:
                v3.append((0, v5))
                a1[0][v5] = 0
            if a1[v1 - 1][v5]:
                v3.append((v1 - 1, v5))
                a1[v1 - 1][v5] = 0
        v6 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while v3:
            v7, v8 = v3.popleft()
            for v9, v10 in v6:
                v11, v12 = (v7 + v9, v8 + v10)
                if 0 <= v11 < v1 and 0 <= v12 < v2 and a1[v11][v12]:
                    a1[v11][v12] = 0
                    v3.append((v11, v12))
        return sum((sum(row) for v13 in a1))
