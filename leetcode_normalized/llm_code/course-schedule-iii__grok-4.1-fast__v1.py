import heapq
import operator

class C1:

    def scheduleCourse(self, a1):
        v1 = sorted(a1, key=operator.itemgetter(1))
        v2 = []
        v3 = 0
        for v4, v5 in v1:
            v3 += v4
            heapq.heappush(v2, -v4)
            if v3 > v5:
                v3 += heapq.heappop(v2)
        return len(v2)
