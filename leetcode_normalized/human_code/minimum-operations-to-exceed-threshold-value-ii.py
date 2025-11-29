import heapq

class C1(object):

    def minOperations(self, a1, a2):
        """
        """
        v1 = 0
        heapq.heapify(a1)
        while a1:
            if a1[0] >= a2:
                break
            v2 = heapq.heappop(a1)
            v3 = heapq.heappop(a1)
            heapq.heappush(a1, 2 * v2 + v3)
            v1 += 1
        return v1
