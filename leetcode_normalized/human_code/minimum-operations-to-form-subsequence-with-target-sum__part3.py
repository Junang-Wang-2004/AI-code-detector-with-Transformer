import heapq

class C1(object):

    def minOperations(self, a1, a2):
        """
        """
        v1 = sum(a1)
        if v1 < a2:
            return -1
        v2 = 0
        v3 = [-x for v4 in a1]
        heapq.heapify(v3)
        while a2:
            v4 = -heapq.heappop(v3)
            if v4 <= a2:
                a2 -= v4
                v1 -= v4
            elif v1 - v4 >= a2:
                v1 -= v4
            else:
                heapq.heappush(v3, -v4 // 2)
                heapq.heappush(v3, -v4 // 2)
                v2 += 1
        return v2
