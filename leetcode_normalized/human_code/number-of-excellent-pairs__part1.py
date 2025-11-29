import collections

class C1(object):

    def countExcellentPairs(self, a1, a2):
        """
        """

        def popcount(a1):
            return bin(a1)[2:].count('1')
        v1 = collections.Counter((popcount(x) for v2 in set(a1)))
        return sum((v1[i] * v1[j] for v3 in v1.keys() for v4 in v1.keys() if v3 + v4 >= a2))
