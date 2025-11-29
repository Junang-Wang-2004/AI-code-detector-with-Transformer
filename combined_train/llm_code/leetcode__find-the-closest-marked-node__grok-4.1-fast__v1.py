import heapq
from collections import defaultdict

class C1:

    def minimumDistance(self, a1, a2, a3, a4):
        v1 = set(a4)
        v2 = defaultdict(list)
        for v3, v4, v5 in a2:
            v2[v3].append((v4, v5))
        v6 = 10 ** 18
        v7 = [v6] * a1
        v7[a3] = 0
        v8 = [(0, a3)]
        while v8:
            v9, v10 = heapq.heappop(v8)
            if v9 > v7[v10]:
                continue
            if v10 in v1:
                return v9
            for v11, v12 in v2[v10]:
                v13 = v9 + v12
                if v13 < v7[v11]:
                    v7[v11] = v13
                    heapq.heappush(v8, (v13, v11))
        return -1
