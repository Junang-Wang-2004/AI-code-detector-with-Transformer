from collections import deque

class C1(object):

    def shortestAlternatingPaths(self, a1, a2, a3):
        v1 = [[] for v2 in range(a1)]
        v3 = [[] for v2 in range(a1)]
        for v4, v5 in a2:
            v1[v4].append(v5)
        for v4, v5 in a3:
            v3[v4].append(v5)
        v6 = 2 * a1 + 5
        v7 = [[v6] * 2 for v2 in range(a1)]
        v7[0][0] = v7[0][1] = 0
        v8 = deque([(0, 0), (0, 1)])
        while v8:
            v9, v10 = v8.popleft()
            v11 = 1 - v10
            v12 = v1[v9] if v10 == 0 else v3[v9]
            for v13 in v12:
                if v7[v13][v10] == v6:
                    v7[v13][v10] = v7[v9][v11] + 1
                    v8.append((v13, v11))
        v14 = []
        for v15 in range(a1):
            v16 = min(v7[v15])
            v14.append(v16 if v16 < v6 else -1)
        return v14
