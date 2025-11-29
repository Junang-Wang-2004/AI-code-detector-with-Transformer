from collections import deque

class C1:

    def maximumMinutes(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v4 = 10 ** 9
        v5 = [[v4] * v2 for v6 in range(v1)]
        v7 = deque()
        for v8 in range(v1):
            for v9 in range(v2):
                if a1[v8][v9] == 1:
                    v5[v8][v9] = 0
                    v7.append((v8, v9, 0))
        while v7:
            v10, v11, v12 = v7.popleft()
            for v13, v14 in v3:
                v15, v16 = (v10 + v13, v11 + v14)
                if 0 <= v15 < v1 and 0 <= v16 < v2 and (a1[v15][v16] != 2) and (v5[v15][v16] == v4):
                    v5[v15][v16] = v12 + 1
                    v7.append((v15, v16, v12 + 1))
        v17 = [[v4] * v2 for v6 in range(v1)]
        v7 = deque([(0, 0, 0)])
        v17[0][0] = 0
        v18, v19 = (v1 - 1, v2 - 1)
        while v7:
            v10, v11, v12 = v7.popleft()
            for v13, v14 in v3:
                v15, v16 = (v10 + v13, v11 + v14)
                if 0 <= v15 < v1 and 0 <= v16 < v2 and (a1[v15][v16] != 2):
                    v20 = v12 + 1
                    v21 = v15 == v18 and v16 == v19 and (v20 <= v5[v15][v16]) or v20 < v5[v15][v16]
                    if v21 and v20 < v17[v15][v16]:
                        v17[v15][v16] = v20
                        v7.append((v15, v16, v20))
        v22 = v17[v18][v19]
        if v22 == v4:
            return -1
        v23 = v5[v18][v19]
        if v23 == v4:
            return v4
        v24 = v23 - v22
        v25, v26 = (v18, v19 - 1)
        v27, v28 = (v18 - 1, v19)
        v29 = v5[v25][v26] - v17[v25][v26]
        v30 = v5[v27][v28] - v17[v27][v28]
        return v24 if v24 + 2 == v29 or v24 + 2 == v30 else v24 - 1
