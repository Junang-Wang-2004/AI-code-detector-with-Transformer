import collections
import heapq

class C1(object):

    def medianSlidingWindow(self, a1, a2):
        """
        """

        def lazy_delete(a1, a2, a3):
            while a1 and a3 * a1[0] in a2:
                a2[a3 * a1[0]] -= 1
                if not a2[a3 * a1[0]]:
                    del a2[a3 * a1[0]]
                heapq.heappop(a1)
        v1, v2 = ([], [])
        for v3 in range(a2):
            if v3 % 2 == 0:
                heapq.heappush(v1, -heapq.heappushpop(v2, -a1[v3]))
            else:
                heapq.heappush(v2, -heapq.heappushpop(v1, a1[v3]))
        v4 = [float(v1[0])] if a2 % 2 else [(v1[0] - v2[0]) / 2.0]
        v5 = collections.defaultdict(int)
        for v3 in range(a2, len(a1)):
            heapq.heappush(v2, -heapq.heappushpop(v1, a1[v3]))
            if a1[v3 - a2] > -v2[0]:
                heapq.heappush(v1, -heapq.heappop(v2))
            v5[a1[v3 - a2]] += 1
            lazy_delete(v2, v5, -1)
            lazy_delete(v1, v5, 1)
            v4.append(float(v1[0]) if a2 % 2 else (v1[0] - v2[0]) / 2.0)
        return v4
