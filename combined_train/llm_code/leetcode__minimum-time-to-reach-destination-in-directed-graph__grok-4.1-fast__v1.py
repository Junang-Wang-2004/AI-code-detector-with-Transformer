import heapq
import sys

class C1(object):

    def minTime(self, a1, a2):
        v1 = sys.maxsize
        v2 = [[] for v3 in range(a1)]
        for v4, v5, v6, cls in a2:
            v2[v4].append((v5, v6, cls))
        v7 = [v1] * a1
        v7[0] = 0
        v8 = [(0, 0)]
        while v8:
            v9, v10 = heapq.heappop(v8)
            if v9 > v7[v10]:
                continue
            for v11, v12, v13 in v2[v10]:
                if v9 > v13:
                    continue
                v14 = max(v9, v12)
                v15 = v14 + 1
                if v15 < v7[v11]:
                    v7[v11] = v15
                    heapq.heappush(v8, (v15, v11))
        v16 = v7[a1 - 1]
        return v16 if v16 != v1 else -1
