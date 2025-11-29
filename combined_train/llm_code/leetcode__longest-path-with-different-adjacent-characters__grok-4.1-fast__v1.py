from collections import deque

class C1:

    def longestPath(self, a1, a2):
        v1 = len(a2)
        v2 = [[] for v3 in range(v1)]
        v4 = [0] * v1
        for v5 in range(1, v1):
            v6 = a1[v5]
            v2[v5].append(v6)
            v4[v6] += 1
        v7 = [[0, 0] for v3 in range(v1)]
        v8 = deque(((v5, 1) for v5 in range(v1) if v4[v5] == 0))
        v9 = 1
        while v8:
            v10 = deque()
            for v11, v12 in v8:
                for v13 in v2[v11]:
                    if a2[v13] != a2[v11]:
                        if v12 > v7[v13][0]:
                            v7[v13][1] = v7[v13][0]
                            v7[v13][0] = v12
                        elif v12 > v7[v13][1]:
                            v7[v13][1] = v12
                    v4[v13] -= 1
                    if v4[v13] == 0:
                        v14 = v7[v13][0] + 1
                        v10.append((v13, v14))
                        v9 = max(v9, v7[v13][0] + v7[v13][1] + 1)
            v8 = v10
        return v9
