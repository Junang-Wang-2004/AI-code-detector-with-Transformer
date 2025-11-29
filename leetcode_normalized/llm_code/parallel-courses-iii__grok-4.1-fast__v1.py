class C1:

    def minimumTime(self, a1, a2, a3):
        v1 = [[] for v2 in range(a1)]
        v3 = [0] * a1
        for v4, v5 in a2:
            v1[v4 - 1].append(v5 - 1)
            v3[v5 - 1] += 1
        from collections import deque
        v6 = deque((i for v7 in range(a1) if v3[v7] == 0))
        v8 = [0] * a1
        for v7 in range(a1):
            if v3[v7] == 0:
                v8[v7] = a3[v7]
        while v6:
            v9 = v6.popleft()
            for v10 in v1[v9]:
                v8[v10] = max(v8[v10], v8[v9] + a3[v10])
                v3[v10] -= 1
                if v3[v10] == 0:
                    v6.append(v10)
        return max(v8)
