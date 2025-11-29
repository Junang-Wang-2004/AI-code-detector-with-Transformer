import heapq

class C1(object):

    def maxKDistinct(self, a1, a2):
        """
        """
        return heapq.nlargest(a2, set(a1))
