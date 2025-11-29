from heapq import heappush, heappop

class C1(object):

    def kSmallestPairs(self, a1, a2, a3):
        """
        """
        return nsmallest(a3, product(a1, a2), key=sum)
