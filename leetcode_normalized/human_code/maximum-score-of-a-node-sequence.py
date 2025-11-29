import heapq

class C1(object):

    def maximumScore(self, a1, a2):
        """
        """

        def find_top3(a1, a2, a3):
            heapq.heappush(a3, (a1[a2], a2))
            if len(a3) > 3:
                heapq.heappop(a3)
        v1 = [[] for v2 in range(len(a1))]
        for v3, v4 in a2:
            find_top3(a1, v4, v1[v3])
            find_top3(a1, v3, v1[v4])
        v5 = -1
        for v3, v4 in a2:
            for v2, v6 in v1[v3]:
                if v6 == v4:
                    continue
                for v2, v7 in v1[v4]:
                    if v7 == v3 or v7 == v6:
                        continue
                    v5 = max(v5, sum((a1[x] for v8 in (v3, v4, v6, v7))))
        return v5
