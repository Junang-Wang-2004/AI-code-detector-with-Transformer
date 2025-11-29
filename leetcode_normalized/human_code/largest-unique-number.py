import collections

class C1(object):

    def largestUniqueNumber(self, a1):
        """
        """
        a1.append(-1)
        return max((k for v1, v2 in list(collections.Counter(a1).items()) if v2 == 1))
