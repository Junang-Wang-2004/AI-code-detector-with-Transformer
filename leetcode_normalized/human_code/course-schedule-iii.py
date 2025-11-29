import collections
import heapq

class C1(object):

    def scheduleCourse(self, a1):
        """
        """
        a1.sort(key=lambda t_end: t_end[1])
        v1 = []
        v2 = 0
        for v3, v4 in a1:
            v2 += v3
            heapq.heappush(v1, -v3)
            if v2 > v4:
                v2 += heapq.heappop(v1)
        return len(v1)
