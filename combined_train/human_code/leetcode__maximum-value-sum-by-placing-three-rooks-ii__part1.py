import heapq
import itertools

class C1(object):

    def maximumValueSum(self, a1):
        """
        """
        v1 = 3
        v2 = [[] for v3 in range(len(a1[0]))]
        for v4 in range(len(a1)):
            v5 = []
            for v6 in range(len(a1[0])):
                heapq.heappush(v5, (a1[v4][v6], v4, v6))
                if len(v5) == v1 + 1:
                    heapq.heappop(v5)
            for v7, v4, v6 in v5:
                heapq.heappush(v2[v6], (v7, v4, v6))
                if len(v2[v6]) == v1 + 1:
                    heapq.heappop(v2[v6])
        v5 = []
        for v8 in v2:
            for v9 in v8:
                heapq.heappush(v5, v9)
                if len(v5) == (v1 - 1) * (2 * v1 - 1) + 1 + 1:
                    heapq.heappop(v5)
        return max((sum((v9[0] for v9 in c)) for v10 in itertools.combinations(v5, v1) if len({v9[1] for v9 in v10}) == v1 == len({v9[2] for v9 in v10})))
