from collections import deque

class C1:

    def getFood(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return -1
        v2 = len(a1[0])
        v3, v4 = next(((i, j) for v5 in range(v1) for v6 in range(v2) if a1[v5][v6] == '*'))
        v7 = deque([(v3, v4, 0)])
        a1[v3][v4] = 'X'
        v8 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while v7:
            v9, v10, v11 = v7.popleft()
            for v12, v13 in v8:
                v14 = v9 + v12
                v15 = v10 + v13
                if 0 <= v14 < v1 and 0 <= v15 < v2 and (a1[v14][v15] != 'X'):
                    if a1[v14][v15] == '#':
                        return v11 + 1
                    a1[v14][v15] = 'X'
                    v7.append((v14, v15, v11 + 1))
        return -1
