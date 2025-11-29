# Time:  O(c * log(mx)), c = cars, mx = max(ranks)
# Space: O(mx)
import collections
import heapq


# freq table, heap, simulation
class Solution2(object):
    def repairCars(self, ranks, cars):
        """
        """
        cnt = collections.Counter(ranks)
        min_heap = [(r*1**2, 1) for r in cnt.keys()]
        heapq.heapify(min_heap)
        while cars > 0:
            t, k = heapq.heappop(min_heap)
            r = t//k**2
            cars -= cnt[r]
            k += 1
            heapq.heappush(min_heap, (r*k**2, k))
        return t
