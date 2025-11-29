import collections

class C1(object):

    def numTriplets(self, a1, a2):
        """
        """

        def two_product(a1, a2):
            v1 = 0
            v2 = collections.defaultdict(int)
            for v3 in a1:
                if a2 % v3:
                    continue
                v1 += v2[a2 // v3]
                v2[v3] += 1
            return v1
        v1 = 0
        for v2 in a1:
            v1 += two_product(a2, v2 ** 2)
        for v2 in a2:
            v1 += two_product(a1, v2 ** 2)
        return v1
