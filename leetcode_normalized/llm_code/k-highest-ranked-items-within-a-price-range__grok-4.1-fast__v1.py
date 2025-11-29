from collections import deque

class C1:

    def highestRankedKItems(self, a1, a2, a3, a4):
        v1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        v2 = len(a1)
        v3 = len(a1[0])
        v4 = [[float('inf')] * v3 for v5 in range(v2)]
        v4[a3[0]][a3[1]] = 0
        v6 = deque([(a3[0], a3[1])])
        while v6:
            v7, v8 = v6.popleft()
            for v9, v10 in v1:
                v11 = v7 + v9
                v12 = v8 + v10
                if 0 <= v11 < v2 and 0 <= v12 < v3 and (a1[v11][v12] != 0) and (v4[v11][v12] == float('inf')):
                    v4[v11][v12] = v4[v7][v8] + 1
                    v6.append((v11, v12))
        v13, v14 = a2
        v15 = []
        for v16 in range(v2):
            for v17 in range(v3):
                if v13 <= a1[v16][v17] <= v14 and v4[v16][v17] < float('inf'):
                    v15.append((v4[v16][v17], a1[v16][v17], v16, v17))
        v15.sort()
        v18 = [[item[2], item[3]] for v19 in v15[:a4]]
        return v18
