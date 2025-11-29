import heapq

class C1(object):

    def kSum(self, a1, a2):
        v1 = 0
        for v2 in a1:
            if v2 > 0:
                v1 += v2
        v3 = []
        for v2 in a1:
            v3.append(abs(v2))
        v3.sort()
        v4 = []
        heapq.heappush(v4, (-v1, 0))
        v5 = 0
        while v5 < a2:
            v6, v7 = heapq.heappop(v4)
            v8 = -v6
            v5 += 1
            if v7 < len(v3):
                v9 = v8 - v3[v7]
                heapq.heappush(v4, (-v9, v7 + 1))
                if v7 > 0:
                    v10 = v8 + v3[v7 - 1] - v3[v7]
                    heapq.heappush(v4, (-v10, v7 + 1))
        return v8
