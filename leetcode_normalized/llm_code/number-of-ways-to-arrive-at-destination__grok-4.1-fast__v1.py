import heapq

class C1(object):

    def countPaths(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = [[] for v3 in range(a1)]
        for v4, v5, v6 in a2:
            v2[v4].append((v5, v6))
            v2[v5].append((v4, v6))
        v7 = [float('inf')] * a1
        v7[0] = 0
        v8 = [0] * a1
        v8[0] = 1
        v9 = [(0, 0)]
        while v9:
            v10, v11 = heapq.heappop(v9)
            if v10 > v7[v11]:
                continue
            for v12, v13 in v2[v11]:
                v14 = v10 + v13
                if v14 < v7[v12]:
                    v7[v12] = v14
                    v8[v12] = v8[v11]
                    heapq.heappush(v9, (v14, v12))
                elif v14 == v7[v12]:
                    v8[v12] = (v8[v12] + v8[v11]) % v1
        return v8[a1 - 1]
