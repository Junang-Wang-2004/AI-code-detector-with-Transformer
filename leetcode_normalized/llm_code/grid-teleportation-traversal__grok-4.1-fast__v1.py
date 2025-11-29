from collections import deque, defaultdict
import math

class C1:

    def minMoves(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return -1
        v2 = len(a1[0])
        v3 = defaultdict(list)
        for v4 in range(v1):
            for v5 in range(v2):
                if a1[v4][v5].isupper():
                    v3[a1[v4][v5]].append((v4, v5))
        v6 = [[math.inf] * v2 for v7 in range(v1)]
        v6[0][0] = 0
        v8 = deque([(0, 0)])
        v9 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while v8:
            v10, v11 = v8.popleft()
            v12 = v6[v10][v11]
            if v10 == v1 - 1 and v11 == v2 - 1:
                return v12
            v13 = a1[v10][v11]
            if v13.isupper():
                for v14, v15 in v3[v13]:
                    if v6[v14][v15] > v12:
                        v6[v14][v15] = v12
                        v8.appendleft((v14, v15))
            for v16, v17 in v9:
                v14, v15 = (v10 + v16, v11 + v17)
                if 0 <= v14 < v1 and 0 <= v15 < v2 and (a1[v14][v15] != '#'):
                    v18 = v12 + 1
                    if v18 < v6[v14][v15]:
                        v6[v14][v15] = v18
                        v8.append((v14, v15))
        return -1
