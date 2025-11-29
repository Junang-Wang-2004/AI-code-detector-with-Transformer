# Time:  O((w * b * 2^b) * log(w * b * 2^b))
# Space: O(w * b * 2^b)
import heapq


class Solution2(object):
    def assignBikes(self, workers, bikes):
        """
        """
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        min_heap = [(0, 0, 0)]
        lookup = set()
        while min_heap:
            cost, i, taken = heapq.heappop(min_heap)
            if (i, taken) in lookup:
                continue
            lookup.add((i, taken))
            if i == len(workers):
                return cost
            for j in range(len(bikes)):
                if taken & (1<<j):
                    continue
                heapq.heappush(min_heap, (cost+manhattan(workers[i], bikes[j]),  # O(b)
                                          i+1,            # O(w)
                                          taken|(1<<j)))  # O(2^b)

