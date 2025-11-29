import heapq

class C1(object):

    def halveArray(self, a1):
        """
        """
        v1 = sum(a1) / 2.0
        v2 = [-x for v3 in a1]
        heapq.heapify(v2)
        v4 = 1
        while v2:
            v3 = -heapq.heappop(v2) / 2.0
            v1 -= v3
            if v1 <= 0.0:
                break
            heapq.heappush(v2, -v3)
            v4 += 1
        return v4
