class C1(object):

    def nthSuperUglyNumber(self, a1, a2):
        """
        """
        v1, v2, v3, v4 = ([0] * a1, [0] * len(a2), [], set([1]))
        v1[0] = 1
        for v5, v6 in enumerate(a2):
            heapq.heappush(v3, (v6, v5))
            v4.add(v6)
        for v7 in range(1, a1):
            v1[v7], v5 = heapq.heappop(v3)
            while a2[v5] * v1[v2[v5]] in v4:
                v2[v5] += 1
            heapq.heappush(v3, (a2[v5] * v1[v2[v5]], v5))
            v4.add(a2[v5] * v1[v2[v5]])
        return v1[-1]
