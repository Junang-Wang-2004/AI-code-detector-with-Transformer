import collections
import heapq

class C1:

    def avoidFlood(self, a1):
        v1 = collections.defaultdict(list)
        for v2, v3 in enumerate(a1):
            if v3:
                v1[v3].append(v2)
        v4 = {v3: 0 for v3 in v1}
        v5 = []
        v6 = []
        for v2 in range(len(a1)):
            v3 = a1[v2]
            if v3 != 0:
                v6.append(-1)
                v7 = v4[v3]
                if v7 + 1 < len(v1[v3]):
                    v8 = v1[v3][v7 + 1]
                    heapq.heappush(v5, (v8, v3))
                    v4[v3] += 1
            elif v5:
                v9, v10 = heapq.heappop(v5)
                if v9 <= v2:
                    return []
                v6.append(v10)
            else:
                v6.append(1)
        return v6 if not v5 else []
