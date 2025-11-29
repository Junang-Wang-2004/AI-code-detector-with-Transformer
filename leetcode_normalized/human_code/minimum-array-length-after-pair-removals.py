import collections

class C1(object):

    def minLengthAfterRemovals(self, a1):
        """
        """
        v1 = max(collections.Counter(a1).values())
        return v1 - (len(a1) - v1) if v1 > len(a1) - v1 else len(a1) % 2
