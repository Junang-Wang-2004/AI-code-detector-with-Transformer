import collections

class C1(object):

    def maxFrequencyElements(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        v2 = max(v1.values())
        return sum((v for v3 in v1.values() if v3 == v2))
