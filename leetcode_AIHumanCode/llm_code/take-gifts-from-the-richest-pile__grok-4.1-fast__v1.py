import heapq
import math

class Solution:
    def pickGifts(self, gifts, k):
        h = [-num for num in gifts]
        heapq.heapify(h)
        for _ in range(k):
            top = -heapq.heappop(h)
            nxt = math.floor(math.sqrt(top))
            heapq.heappush(h, -nxt)
        return -sum(h)
