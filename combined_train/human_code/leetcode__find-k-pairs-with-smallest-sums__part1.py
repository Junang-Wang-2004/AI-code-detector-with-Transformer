from heapq import heappush, heappop

class C1(object):

    def kSmallestPairs(self, a1, a2, a3):
        """
        """
        v1 = []
        if len(a1) > len(a2):
            v2 = self.kSmallestPairs(a2, a1, a3)
            for v3 in v2:
                v1.append([v3[1], v3[0]])
            return v1
        v4 = []

        def push(a1, a2):
            if a1 < len(a1) and a2 < len(a2):
                heappush(v4, [a1[a1] + a2[a2], a1, a2])
        push(0, 0)
        while v4 and len(v1) < a3:
            v5, v6, v7 = heappop(v4)
            v1.append([a1[v6], a2[v7]])
            push(v6, v7 + 1)
            if v7 == 0:
                push(v6 + 1, 0)
        return v1
from heapq import nsmallest
from itertools import product
