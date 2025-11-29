import heapq

class C1(object):

    def minAvailableDuration(self, a1, a2, a3):
        """
        """
        v1 = list([slot for v2 in a1 + a2 if v2[1] - v2[0] >= a3])
        heapq.heapify(v1)
        while len(v1) > 1:
            v3 = heapq.heappop(v1)
            v4 = v1[0]
            if v3[1] - v4[0] >= a3:
                return [v4[0], v4[0] + a3]
        return []
