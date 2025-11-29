import heapq

class C1(object):

    def kClosest(self, a1, a2):
        """
        """

        def dist(a1):
            return a1[0] ** 2 + a1[1] ** 2
        v1 = []
        for v2 in a1:
            heapq.heappush(v1, (-dist(v2), v2))
            if len(v1) > a2:
                heapq.heappop(v1)
        return [heapq.heappop(v1)[1] for v3 in range(len(v1))]
