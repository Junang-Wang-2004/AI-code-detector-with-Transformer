import itertools

class C1(object):

    def canSortArray(self, a1):
        """
        """

        def popcount(a1):
            return bin(a1).count('1')

        def pairwise(a1):
            v1, v2 = tee(a1)
            next(v2, None)
            return zip(v1, v2)
        return all((max(a) <= min(b) for v1, v2 in pairwise((list(it) for v3, v4 in groupby(a1, popcount)))))
