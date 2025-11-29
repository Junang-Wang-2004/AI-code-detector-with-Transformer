import heapq

class C1(object):

    def maxRunTime(self, a1, a2):
        """
        """
        v1 = sum(a2)
        for v2 in range(len(a2)):
            a2[v2] = -a2[v2]
        heapq.heapify(a2)
        while -a2[0] > v1 // a1:
            a1 -= 1
            v1 -= -heapq.heappop(a2)
        return v1 // a1
