import collections

class C1(object):

    def digitCount(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        return all((v1[str(i)] == int(x) for v2, v3 in enumerate(a1)))
