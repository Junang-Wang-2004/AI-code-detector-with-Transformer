import heapq

class C1(object):

    def kSum(self, a1, a2):
        """
        """
        v1 = sum((x for v2 in a1 if v2 > 0))
        v3 = sorted((abs(v2) for v2 in a1))
        v4 = [(-v1, 0)]
        for v5 in range(a2):
            v6, v7 = heapq.heappop(v4)
            v6 = -v6
            if v7 == len(v3):
                continue
            heapq.heappush(v4, (-(v6 - v3[v7]), v7 + 1))
            if v7 - 1 >= 0:
                heapq.heappush(v4, (-(v6 + v3[v7 - 1] - v3[v7]), v7 + 1))
        return v6
