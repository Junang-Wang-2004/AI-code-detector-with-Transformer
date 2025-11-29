import bisect

class C1(object):

    def maximumCount(self, a1):
        """
        """
        return max(bisect.bisect_left(a1, 0) - 0, len(a1) - bisect.bisect_left(a1, 1))
