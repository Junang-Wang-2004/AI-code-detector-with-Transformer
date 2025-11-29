import heapq

class C1(object):

    def maxProbability(self, a1, a2, a3, a4, a5):
        v1 = [[] for v2 in range(a1)]
        for v3, (v4, v5) in enumerate(a2):
            v6 = a3[v3]
            v1[v4].append((v5, v6))
            v1[v5].append((v4, v6))
        v7 = [0.0] * a1
        v7[a4] = 1.0
        v8 = [(-1.0, a4)]
        v9 = [False] * a1
        while v8:
            v10, v11 = heapq.heappop(v8)
            if v9[v11]:
                continue
            v9[v11] = True
            v12 = -v10
            for v13, v14 in v1[v11]:
                v15 = v12 * v14
                if v15 > v7[v13]:
                    v7[v13] = v15
                    heapq.heappush(v8, (-v15, v13))
        return v7[a5]
