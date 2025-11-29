import collections

class C1(object):

    def findLeastNumOfUniqueInts(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1)
        v2, v3 = (len(v1), collections.Counter(iter(v1.values())))
        for v4 in range(1, len(a1) + 1):
            if a2 < v4 * v3[v4]:
                v2 -= a2 // v4
                break
            a2 -= v4 * v3[v4]
            v2 -= v3[v4]
        return v2
