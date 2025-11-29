import heapq

class C1(object):

    def minimumCoins(self, a1):
        v1 = len(a1)
        v2 = [float('inf')] * (v1 + 1)
        v2[0] = 0
        v3 = []
        for v4 in range(v1):
            heapq.heappush(v3, (v2[v4] + a1[v4], v4))
            v5 = v4 // 2
            while v3 and v3[0][1] < v5:
                heapq.heappop(v3)
            v2[v4 + 1] = v3[0][0]
        return v2[v1]
