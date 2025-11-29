from collections import deque

class C1:

    def findOrder(self, a1, a2):
        v1 = a1
        v2 = [[] for v3 in range(v1)]
        v4 = [0] * v1
        for v5, v6 in a2:
            v2[v6].append(v5)
            v4[v5] += 1
        v7 = deque((i for v8 in range(v1) if v4[v8] == 0))
        v9 = []
        while v7:
            v10 = v7.popleft()
            v9.append(v10)
            for v11 in v2[v10]:
                v4[v11] -= 1
                if v4[v11] == 0:
                    v7.append(v11)
        return v9 if len(v9) == v1 else []
