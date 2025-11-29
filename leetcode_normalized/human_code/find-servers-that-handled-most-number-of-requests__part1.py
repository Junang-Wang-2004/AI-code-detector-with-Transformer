import itertools
import heapq

class C1(object):

    def busiestServers(self, a1, a2, a3):
        """
        """
        v1 = [0] * a1
        v2 = []
        v3 = []
        v4 = list(range(a1))
        for v5, (v6, v7) in enumerate(zip(a2, a3)):
            if v5 % a1 == 0:
                v4, v3 = ([], v4)
            while v2 and v2[0][0] <= v6:
                v8, v9 = heapq.heappop(v2)
                if v9 < v5 % a1:
                    heapq.heappush(v4, v9)
                else:
                    heapq.heappush(v3, v9)
            v10 = v3 if v3 else v4
            if not v10:
                continue
            v11 = heapq.heappop(v10)
            v1[v11] += 1
            heapq.heappush(v2, (v6 + v7, v11))
        v12 = max(v1)
        return [v5 for v5 in range(a1) if v1[v5] == v12]
