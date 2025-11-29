from collections import deque

class C1:

    def maximumSafenessFactor(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = len(a1[0])
        v3 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        v4 = v1 + v2
        v5 = [[v4] * v2 for v6 in range(v1)]
        v7 = deque()
        for v8 in range(v1):
            for v9 in range(v2):
                if a1[v8][v9] == 1:
                    v5[v8][v9] = 0
                    v7.append((v8, v9))
        while v7:
            v10, v11 = v7.popleft()
            for v12, v13 in v3:
                v14, v15 = (v10 + v12, v11 + v13)
                if 0 <= v14 < v1 and 0 <= v15 < v2 and (v5[v14][v15] > v5[v10][v11] + 1):
                    v5[v14][v15] = v5[v10][v11] + 1
                    v7.append((v14, v15))

        def feasible(a1):
            if v5[0][0] < a1 or v5[v1 - 1][v2 - 1] < a1:
                return False
            v1 = [[False] * v2 for v6 in range(v1)]
            v2 = deque([(0, 0)])
            v1[0][0] = True
            while v2:
                v3, v4 = v2.popleft()
                if v3 == v1 - 1 and v4 == v2 - 1:
                    return True
                for v5, v6 in v3:
                    v7, v8 = (v3 + v5, v4 + v6)
                    if 0 <= v7 < v1 and 0 <= v8 < v2 and (not v1[v7][v8]) and (v5[v7][v8] >= a1):
                        v1[v7][v8] = True
                        v2.append((v7, v8))
            return False
        v16, v17 = (0, max(map(max, v5)) + 1)
        while v16 < v17:
            v18 = (v16 + v17 + 1) // 2
            if feasible(v18):
                v16 = v18
            else:
                v17 = v18 - 1
        return v16
