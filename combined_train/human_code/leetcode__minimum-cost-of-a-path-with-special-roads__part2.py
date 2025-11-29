import collections
import heapq

class C1(object):

    def minimumCost(self, a1, a2, a3):
        """
        """
        a1, a2 = (tuple(a1), tuple(a2))
        v3 = collections.defaultdict(list, {a2: []})
        for v4, v5, v6, v7, v8 in a3:
            v3[v4, v5].append((v6, v7, v8))
        v9 = [(0, a1)]
        v10 = {a1: 0}
        while v9:
            v11, (v4, v5) = heapq.heappop(v9)
            if v11 > v10[v4, v5]:
                continue
            if (v4, v5) == a2:
                return v11
            for v6, v7, v8 in v3[v4, v5]:
                if not ((v6, v7) not in v10 or v10[v6, v7] > v11 + v8):
                    continue
                v10[v6, v7] = v11 + v8
                heapq.heappush(v9, (v10[v6, v7], (v6, v7)))
            for v6, v7 in v3.keys():
                if not ((v6, v7) not in v10 or v10[v6, v7] > v11 + abs(v6 - v4) + abs(v7 - v5)):
                    continue
                v10[v6, v7] = v11 + abs(v6 - v4) + abs(v7 - v5)
                heapq.heappush(v9, (v10[v6, v7], (v6, v7)))
        return -1
