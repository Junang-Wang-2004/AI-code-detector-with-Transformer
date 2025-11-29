import heapq

class C1(object):

    def rangeSum(self, a1, a2, a3, a4):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = []
        for v3, v4 in enumerate(a1, 1):
            heapq.heappush(v2, (v4, v3))
        v5 = 0
        for v3 in range(1, a4 + 1):
            v6, v7 = heapq.heappop(v2)
            if v3 >= a3:
                v5 = (v5 + v6) % v1
            if v7 + 1 <= a2:
                heapq.heappush(v2, (v6 + a1[v7], v7 + 1))
        return v5
