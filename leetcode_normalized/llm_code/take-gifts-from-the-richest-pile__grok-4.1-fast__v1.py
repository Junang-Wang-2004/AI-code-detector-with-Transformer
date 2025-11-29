import heapq
import math

class C1:

    def pickGifts(self, a1, a2):
        v1 = [-num for v2 in a1]
        heapq.heapify(v1)
        for v3 in range(a2):
            v4 = -heapq.heappop(v1)
            v5 = math.floor(math.sqrt(v4))
            heapq.heappush(v1, -v5)
        return -sum(v1)
