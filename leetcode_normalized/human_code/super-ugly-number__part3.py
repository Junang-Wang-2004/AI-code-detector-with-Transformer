class C1(object):

    def nthSuperUglyNumber(self, a1, a2):
        """
        """
        v1, v2, v3 = ([1], [0] * len(a2), [])
        for v4, v5 in enumerate(a2):
            heapq.heappush(v3, (v5, v4))
        for v6 in range(1, a1):
            v7, v4 = v3[0]
            v1 += [v7]
            while v3[0][0] == v7:
                v7, v4 = heapq.heappop(v3)
                v2[v4] += 1
                heapq.heappush(v3, (a2[v4] * v1[v2[v4]], v4))
        return v1[-1]
