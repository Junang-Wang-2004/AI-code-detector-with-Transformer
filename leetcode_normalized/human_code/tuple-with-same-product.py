import collections

class C1(object):

    def tupleSameProduct(self, a1):
        """
        """
        v1 = 0
        v2 = collections.Counter()
        for v3 in range(len(a1)):
            for v4 in range(v3 + 1, len(a1)):
                v1 += v2[a1[v3] * a1[v4]]
                v2[a1[v3] * a1[v4]] += 1
        return 8 * v1
