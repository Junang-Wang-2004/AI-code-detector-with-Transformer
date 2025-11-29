import collections

class C1(object):

    def reorderedPowerOf2(self, a1):
        """
        """
        v1 = collections.Counter(str(a1))
        return any((v1 == collections.Counter(str(1 << i)) for v2 in range(31)))
