import collections
import heapq
from math import inf

class C1:

    def minimumCost(self, a1, a2, a3):
        v1 = tuple(a1)
        v2 = tuple(a2)
        v3 = collections.defaultdict(list)
        v3[v2] = []
        for v4, v5, v6, v7, v8 in a3:
            v3[v4, v5].append(((v6, v7), v8))
        v9 = list(v3.keys())
        v10 = {}
        v11 = []
        heapq.heappush(v11, (0, v1))
        v10[v1] = 0
        while v11:
            v12, v13 = heapq.heappop(v11)
            if v12 > v10.get(v13, inf):
                continue
            if v13 == v2:
                return v12
            for v14, v8 in v3[v13]:
                v15 = v12 + v8
                if v15 < v10.get(v14, inf):
                    v10[v14] = v15
                    heapq.heappush(v11, (v15, v14))
            for v16 in v9:
                v17 = abs(v13[0] - v16[0]) + abs(v13[1] - v16[1])
                v15 = v12 + v17
                if v15 < v10.get(v16, inf):
                    v10[v16] = v15
                    heapq.heappush(v11, (v15, v16))
        return v10.get(v2, inf)
