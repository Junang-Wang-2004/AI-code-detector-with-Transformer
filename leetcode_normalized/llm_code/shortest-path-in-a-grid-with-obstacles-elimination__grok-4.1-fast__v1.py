class C1(object):

    def shortestPath(self, a1, a2):
        v1, v2 = (len(a1), len(a1[0]))
        from collections import deque
        v3 = deque()
        v4 = [[[False] * (a2 + 1) for v5 in range(v2)] for v5 in range(v1)]
        v3.append((0, 0, a2, 0))
        v4[0][0][a2] = True
        v6 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while v3:
            v7, v8, v9, v10 = v3.popleft()
            if v7 == v1 - 1 and v8 == v2 - 1:
                return v10
            for v11, v12 in v6:
                v13, v14 = (v7 + v11, v8 + v12)
                if 0 <= v13 < v1 and 0 <= v14 < v2:
                    v15 = a1[v13][v14]
                    if v15 == 1 and v9 == 0:
                        continue
                    v16 = v9 - v15
                    if not v4[v13][v14][v16]:
                        v4[v13][v14][v16] = True
                        v3.append((v13, v14, v16, v10 + 1))
        return -1
