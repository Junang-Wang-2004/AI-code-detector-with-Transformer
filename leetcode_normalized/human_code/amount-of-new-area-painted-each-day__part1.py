import collections
import heapq

class C1(object):

    def amountPainted(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        for v2, (v3, v4) in enumerate(a1):
            v1[v3].append((True, v2))
            v1[v4].append((False, v2))
        v5 = []
        v6 = [False] * len(a1)
        v7 = [0] * len(a1)
        v8 = -1
        for v9 in sorted(v1.keys()):
            while v5 and v6[v5[0]]:
                heapq.heappop(v5)
            if v5:
                v7[v5[0]] += v9 - v8
            v8 = v9
            for v10, v2 in v1[v9]:
                if v10:
                    heapq.heappush(v5, v2)
                else:
                    v6[v2] = True
        return v7
