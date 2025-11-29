import heapq

class C1(object):

    def isPossible(self, a1):
        """
        """
        v1 = sum(a1)
        v2 = [-x for v3 in a1]
        heapq.heapify(v2)
        while v1 != len(a1):
            v4 = -heapq.heappop(v2)
            v5 = v1 - v4
            v3 = v4 - v5
            if v3 <= 0:
                return False
            if v3 > v5:
                v3 = v3 % v5 + v5
            heapq.heappush(v2, -v3)
            v1 = v3 + v5
        return True
