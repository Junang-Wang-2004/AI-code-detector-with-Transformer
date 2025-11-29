from collections import deque

class C1:

    def loudAndRich(self, a1, a2):
        v1 = len(a2)
        v2 = [[] for v3 in range(v1)]
        for v4, v5 in a1:
            v2[v4].append(v5)
        v6 = [0] * v1
        for v7 in range(v1):
            for v8 in v2[v7]:
                v6[v8] += 1
        v9 = deque((v7 for v7 in range(v1) if v6[v7] == 0))
        v10 = list(range(v1))
        while v9:
            v11 = v9.popleft()
            for v12 in v2[v11]:
                if a2[v10[v11]] < a2[v10[v12]]:
                    v10[v12] = v10[v11]
                v6[v12] -= 1
                if v6[v12] == 0:
                    v9.append(v12)
        return v10
