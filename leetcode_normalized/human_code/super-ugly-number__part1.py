import heapq

class C1(object):

    def nthSuperUglyNumber(self, a1, a2):
        """
        """
        v1, v2, v3, v4 = ([], [0] * a1, [0] * len(a2), [0] * a1)
        v2[0] = 1
        for v5, v6 in enumerate(a2):
            heapq.heappush(v1, (v6, v5))
        for v7 in range(1, a1):
            v2[v7], v5 = heapq.heappop(v1)
            v4[v7] = v5
            v3[v5] += 1
            while v4[v3[v5]] > v5:
                v3[v5] += 1
            heapq.heappush(v1, (a2[v5] * v2[v3[v5]], v5))
        return v2[-1]
