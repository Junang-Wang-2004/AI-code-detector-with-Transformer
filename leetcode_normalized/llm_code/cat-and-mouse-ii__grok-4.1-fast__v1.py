from collections import deque

class C1:

    def canMouseWin(self, a1, a2, a3):
        v1 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        v2, v3 = (len(a1), len(a1[0]))
        v4 = v2 * v3
        v5 = [False] * v4
        v6, v7, v8 = (-1, -1, -1)
        for v9 in range(v2):
            for v10 in range(v3):
                v11 = v9 * v3 + v10
                v12 = a1[v9][v10]
                if v12 == '#':
                    v5[v11] = True
                elif v12 == 'F':
                    v6 = v11
                elif v12 == 'M':
                    v7 = v11
                elif v12 == 'C':
                    v8 = v11
        v13 = [set() for v14 in range(v4)]
        v15 = [set() for v14 in range(v4)]
        for v9 in range(v2):
            for v10 in range(v3):
                v11 = v9 * v3 + v10
                if v5[v11]:
                    continue
                v13[v11].add(v11)
                v15[v11].add(v11)
                for v16, v17 in v1:
                    v18, v19 = (v9 + v16, v10 + v17)
                    v20 = 1
                    while v20 <= a3 and 0 <= v18 < v2 and (0 <= v19 < v3) and (not v5[v18 * v3 + v19]):
                        v13[v11].add(v18 * v3 + v19)
                        v18 += v16
                        v19 += v17
                        v20 += 1
                    v18, v19 = (v9 + v16, v10 + v17)
                    v20 = 1
                    while v20 <= a2 and 0 <= v18 < v2 and (0 <= v19 < v3) and (not v5[v18 * v3 + v19]):
                        v15[v11].add(v18 * v3 + v19)
                        v18 += v16
                        v19 += v17
                        v20 += 1
        v21, v22 = (0, 1)
        v23, v24 = (1, 2)
        v25 = [[[0] * 2 for v14 in range(v4)] for v14 in range(v4)]
        v26 = [[len(v15[j]) for v27 in range(v4)] for v14 in range(v4)]
        v28 = deque()
        for v27 in range(v4):
            if v5[v27] or v27 == v6:
                continue
            v25[v6][v27][v22] = v23
            v28.append((v6, v27, v22))
            v25[v27][v6][v21] = v24
        for v27 in range(v4):
            if v5[v27] or v27 == v6:
                continue
            v25[v27][v27][v21] = v24
            v25[v27][v27][v22] = v24
        while v28:
            v29, v30, v31 = v28.popleft()
            if v31 == v22:
                for v32 in v13[v29]:
                    v33 = v21
                    v34 = v30
                    if v25[v32][v34][v33]:
                        continue
                    v25[v32][v34][v33] = v23
                    v28.append((v32, v34, v33))
            else:
                for v34 in v15[v30]:
                    v33 = v22
                    v32 = v29
                    if v25[v32][v34][v33]:
                        continue
                    v26[v32][v34] -= 1
                    if v26[v32][v34] == 0:
                        v25[v32][v34][v33] = v23
                        v28.append((v32, v34, v33))
        return v25[v7][v8][v21] == v23
