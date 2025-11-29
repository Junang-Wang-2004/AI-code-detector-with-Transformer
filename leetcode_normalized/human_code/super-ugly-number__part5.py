class C1(object):

    def nthSuperUglyNumber(self, a1, a2):
        """
        """
        v1 = 0
        v2 = []
        heapq.heappush(v2, 1)
        for v3 in a2:
            heapq.heappush(v2, v3)
        for v4 in range(a1):
            v1 = heapq.heappop(v2)
            for v5 in range(len(a2)):
                if v1 % a2[v5] == 0:
                    for v6 in range(v5 + 1):
                        heapq.heappush(v2, v1 * a2[v6])
                    break
        return v1
