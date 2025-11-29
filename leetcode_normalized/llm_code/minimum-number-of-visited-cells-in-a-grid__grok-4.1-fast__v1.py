from collections import deque

class C1:

    def minimumVisitedCells(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return -1
        v2 = len(a1[0])
        v3 = 10 ** 9 + 7
        v4 = [[v3] * v2 for v5 in range(v1)]
        v4[0][0] = 1
        v6 = deque([(0, 0)])
        while v6:
            v7, v8 = v6.popleft()
            v9 = v4[v7][v8]
            v10 = a1[v7][v8]
            v11 = min(v7 + v10 + 1, v1)
            v12 = min(v8 + v10 + 1, v2)
            for v13 in range(v7 + 1, v11):
                if v4[v13][v8] > v9 + 1:
                    v4[v13][v8] = v9 + 1
                    v6.append((v13, v8))
            for v14 in range(v8 + 1, v12):
                if v4[v7][v14] > v9 + 1:
                    v4[v7][v14] = v9 + 1
                    v6.append((v7, v14))
        return v4[v1 - 1][v2 - 1] if v4[v1 - 1][v2 - 1] < v3 else -1
