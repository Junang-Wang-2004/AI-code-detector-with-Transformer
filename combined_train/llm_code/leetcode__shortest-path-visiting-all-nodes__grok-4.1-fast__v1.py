import collections

class C1:

    def shortestPathLength(self, a1):
        v1 = len(a1)
        v2 = (1 << v1) - 1
        v3 = {}
        v4 = collections.deque()
        for v5 in range(v1):
            v6 = 1 << v5
            v3[v6, v5] = 0
            v4.append((v6, v5))
        while v4:
            v6, v7 = v4.popleft()
            v8 = v3[v6, v7]
            for v9 in a1[v7]:
                v10 = v6 | 1 << v9
                v11 = (v10, v9)
                if v11 not in v3:
                    v3[v11] = v8 + 1
                    v4.append(v11)
        v12 = float('inf')
        for v13 in range(v1):
            v14 = (v2, v13)
            if v14 in v3:
                v12 = min(v12, v3[v14])
        return v12
