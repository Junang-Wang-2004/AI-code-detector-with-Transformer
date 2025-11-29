import collections

class C1:

    def maxDistance(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = v1 * v2
        v4 = []
        for v5 in range(v1):
            for v6 in range(v2):
                if a1[v5][v6] == 1:
                    v4.append((v5, v6))
        if len(v4) == v3:
            return -1
        v7 = collections.deque(v4)
        v8 = [[False] * v2 for v9 in range(v1)]
        for v5, v6 in v4:
            v8[v5][v6] = True
        v10 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        v11 = 0
        while v7:
            v12 = len(v7)
            for v9 in range(v12):
                v13, v14 = v7.popleft()
                for v15, v16 in v10:
                    v17, v18 = (v13 + v15, v14 + v16)
                    if 0 <= v17 < v1 and 0 <= v18 < v2 and (not v8[v17][v18]) and (a1[v17][v18] == 0):
                        v8[v17][v18] = True
                        v7.append((v17, v18))
            v11 += 1
        return v11 - 1
