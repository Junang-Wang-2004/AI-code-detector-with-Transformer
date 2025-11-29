import collections

class C1(object):

    def canBeEqual(self, a1, a2):
        """
        """
        return all((collections.Counter((a1[j] for v1 in range(i, len(a1), 2))) == collections.Counter((a2[v1] for v1 in range(i, len(a2), 2))) for v2 in range(2)))
