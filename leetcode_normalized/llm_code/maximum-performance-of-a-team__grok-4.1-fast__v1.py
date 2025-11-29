import heapq

class C1(object):

    def maxPerformance(self, a1, a2, a3, a4):
        v1 = 10 ** 9 + 7
        v2 = 0
        v3 = 0
        v4 = []
        v5 = sorted(range(a1), key=lambda i: -a3[i])
        for v6 in v5:
            v7 = a2[v6]
            v8 = a3[v6]
            v3 += v7
            heapq.heappush(v4, v7)
            if len(v4) > a4:
                v3 -= heapq.heappop(v4)
            v2 = max(v2, v3 * v8)
        return v2 % v1
