from collections import deque

class C1:

    def eventualSafeNodes(self, a1):
        v1 = len(a1)
        v2 = [[] for v3 in range(v1)]
        v4 = [0] * v1
        for v5 in range(v1):
            v4[v5] = len(a1[v5])
            for v6 in a1[v5]:
                v2[v6].append(v5)
        v7 = deque((v5 for v5 in range(v1) if v4[v5] == 0))
        v8 = [False] * v1
        while v7:
            v5 = v7.popleft()
            v8[v5] = True
            for v6 in v2[v5]:
                v4[v6] -= 1
                if v4[v6] == 0:
                    v7.append(v6)
        return [i for v9 in range(v1) if v8[v9]]
