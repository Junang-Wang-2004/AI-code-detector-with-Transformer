from collections import deque

class C1:

    def minFlips(self, a1):
        if not a1 or not a1[0]:
            return 0
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = v1 * v2

        def cell(a1, a2):
            return a1 * v2 + a2
        v4 = 0
        for v5 in range(v1):
            for v6 in range(v2):
                if a1[v5][v6]:
                    v4 |= 1 << cell(v5, v6)
        v7 = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]
        v8 = [0] * v3
        for v9 in range(v1):
            for v10 in range(v2):
                v11 = cell(v9, v10)
                v12 = 0
                for v13, v14 in v7:
                    v15 = v9 + v13
                    v16 = v10 + v14
                    if 0 <= v15 < v1 and 0 <= v16 < v2:
                        v12 |= 1 << cell(v15, v16)
                v8[v11] = v12
        v17 = deque([(v4, 0)])
        v18 = {v4}
        while v17:
            v19, v20 = v17.popleft()
            if v19 == 0:
                return v20
            for v21 in v8:
                v22 = v19 ^ v21
                if v22 not in v18:
                    v18.add(v22)
                    v17.append((v22, v20 + 1))
        return -1
