import heapq

class C1:

    def convertArray(self, a1):

        def calc_cost(a1):
            v1 = 0
            v2 = []
            for v3 in a1:
                if v2 and -v2[0] > v3:
                    v4 = -heapq.heappop(v2)
                    v1 += v4 - v3
                    heapq.heappush(v2, -v3)
                heapq.heappush(v2, -v3)
            return v1
        v1 = calc_cost(a1)
        v2 = calc_cost(reversed(a1))
        return min(v1, v2)
