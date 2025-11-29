import sortedcontainers
import itertools
import heapq

class C1(object):

    def busiestServers(self, a1, a2, a3):
        """
        """
        v1 = [0] * a1
        v2 = []
        v3 = sortedcontainers.SortedList(range(a1))
        for v4, (v5, v6) in enumerate(zip(a2, a3)):
            while v2 and v2[0][0] <= v5:
                v7, v8 = heapq.heappop(v2)
                v3.add(v8)
            if not v3:
                continue
            v9 = v3.bisect_left(v4 % a1) % len(v3)
            v10 = v3.pop(v9)
            v1[v10] += 1
            heapq.heappush(v2, (v5 + v6, v10))
        v11 = max(v1)
        return [v4 for v4 in range(a1) if v1[v4] == v11]
