import heapq

class C1(object):

    def leftmostBuildingQueries(self, a1, a2):
        """
        """
        v1 = [-1] * len(a2)
        v2 = [[] for v3 in range(len(a1))]
        for v4, (v5, v6) in enumerate(a2):
            if v5 > v6:
                v5, v6 = (v6, v5)
            if v5 == v6 or a1[v5] < a1[v6]:
                v1[v4] = v6
            else:
                v2[v6].append((a1[v5], v4))
        v7 = []
        for v4, v8 in enumerate(a1):
            for v9 in v2[v4]:
                heapq.heappush(v7, v9)
            while v7 and v7[0][0] < v8:
                v3, v10 = heapq.heappop(v7)
                v1[v10] = v4
        return v1
