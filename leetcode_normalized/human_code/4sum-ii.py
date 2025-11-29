import collections

class C1(object):

    def fourSumCount(self, a1, a2, a3, a4):
        """
        """
        v1 = collections.Counter((a + b for v2 in a1 for v3 in a2))
        return sum((v1[-c - d] for v4 in a3 for v5 in a4))
