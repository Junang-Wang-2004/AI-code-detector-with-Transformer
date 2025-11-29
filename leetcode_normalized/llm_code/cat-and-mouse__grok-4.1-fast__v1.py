from collections import deque

class C1:

    def catMouseGame(self, a1):
        v1 = len(a1)
        v2 = [[[0] * 2 for v3 in range(v1)] for v3 in range(v1)]
        v4 = [[[0] * 2 for v3 in range(v1)] for v3 in range(v1)]
        v5 = set(a1[0])
        v6, v7 = (0, 1)
        for v8 in range(v1):
            for v9 in range(v1):
                v4[v8][v9][v6] = len(a1[v8])
                v10 = len(a1[v9])
                if v9 in v5:
                    v10 -= 1
                v4[v8][v9][v7] = v10
        v11 = deque()
        for v9 in range(1, v1):
            v2[0][v9][v7] = 1
            v11.append((0, v9, v7))
        for v12 in range(1, v1):
            v2[v12][v12][v6] = 2
            v11.append((v12, v12, v6))
            v2[v12][v12][v7] = 2
            v11.append((v12, v12, v7))
        while v11:
            v13, v14, v15 = v11.popleft()
            v16 = v2[v13][v14][v15]
            if v15 == v7:
                for v17 in a1[v13]:
                    v18, v19, v20 = (v17, v14, v6)
                    if v2[v18][v19][v20] != 0:
                        continue
                    if v20 == v16:
                        v2[v18][v19][v20] = v16
                        v11.append((v18, v19, v20))
                    else:
                        v4[v18][v19][v20] -= 1
                        if v4[v18][v19][v20] == 0:
                            v2[v18][v19][v20] = v16
                            v11.append((v18, v19, v20))
            else:
                for v21 in a1[v14]:
                    if v21 == 0:
                        continue
                    v18, v19, v20 = (v13, v21, v7)
                    if v2[v18][v19][v20] != 0:
                        continue
                    if v20 == v16:
                        v2[v18][v19][v20] = v16
                        v11.append((v18, v19, v20))
                    else:
                        v4[v18][v19][v20] -= 1
                        if v4[v18][v19][v20] == 0:
                            v2[v18][v19][v20] = v16
                            v11.append((v18, v19, v20))
        return v2[1][2][v6]
