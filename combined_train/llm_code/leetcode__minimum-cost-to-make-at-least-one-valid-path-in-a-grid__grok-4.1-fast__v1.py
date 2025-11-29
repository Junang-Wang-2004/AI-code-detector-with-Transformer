import collections

class C1:

    def minCost(self, a1):
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = float('inf')
        v4 = [[v3] * v2 for v5 in range(v1)]
        v4[0][0] = 0
        v6 = collections.deque([(0, 0)])
        v7 = [(0, 1, 1), (0, -1, 2), (1, 0, 3), (-1, 0, 4)]
        while v6:
            v8, v9 = v6.popleft()
            if v8 == v1 - 1 and v9 == v2 - 1:
                return v4[v8][v9]
            for v10, v11, v12 in v7:
                v13, v14 = (v8 + v10, v9 + v11)
                if 0 <= v13 < v1 and 0 <= v14 < v2:
                    v15 = 0 if v12 == a1[v8][v9] else 1
                    v16 = v4[v8][v9] + v15
                    if v16 < v4[v13][v14]:
                        v4[v13][v14] = v16
                        if v15 == 0:
                            v6.appendleft((v13, v14))
                        else:
                            v6.append((v13, v14))
        return -1
