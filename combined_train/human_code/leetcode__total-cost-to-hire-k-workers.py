import heapq

class C1(object):

    def totalCost(self, a1, a2, a3):
        """
        """
        v1, v2 = (a3, max(len(a1) - a3, a3) - 1)
        v3, v4 = (a1[:v1], a1[v2 + 1:])
        (heapq.heapify(v3), heapq.heapify(v4))
        v5 = 0
        for v6 in range(a2):
            if not v4 or (v3 and v3[0] <= v4[0]):
                v5 += heapq.heappop(v3)
                if v1 <= v2:
                    heapq.heappush(v3, a1[v1])
                    v1 += 1
            else:
                v5 += heapq.heappop(v4)
                if v1 <= v2:
                    heapq.heappush(v4, a1[v2])
                    v2 -= 1
        return v5
