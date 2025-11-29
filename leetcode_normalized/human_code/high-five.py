import collections
import heapq

class C1(object):

    def highFive(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        for v2, v3 in a1:
            heapq.heappush(v1[v2], v3)
            if len(v1[v2]) > 5:
                heapq.heappop(v1[v2])
        return [[v2, sum(v1[v2]) // len(v1[v2])] for v2 in sorted(v1)]
