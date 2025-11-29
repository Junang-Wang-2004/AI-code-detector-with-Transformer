from collections import deque

class C1:

    def distanceToCycle(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [len(v1[i]) for v6 in range(a1)]
        v7 = deque((v6 for v6 in range(a1) if v5[v6] == 1))
        while v7:
            v8 = v7.popleft()
            v5[v8] = 0
            for v9 in v1[v8]:
                if v5[v9] > 0:
                    v5[v9] -= 1
                    if v5[v9] == 1:
                        v7.append(v9)
        v10 = [v6 for v6 in range(a1) if v5[v6] > 0]
        v11 = [-1] * a1
        v12 = deque(v10)
        for v13 in v10:
            v11[v13] = 0
        while v12:
            v8 = v12.popleft()
            for v9 in v1[v8]:
                if v11[v9] == -1:
                    v11[v9] = v11[v8] + 1
                    v12.append(v9)
        return v11
