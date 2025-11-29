import collections

class C1(object):

    def distance(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2, v3 = (collections.Counter(), collections.Counter())
        for v4 in range(len(a1)):
            v1[v4] += v2[a1[v4]] * v4 - v3[a1[v4]]
            v2[a1[v4]] += 1
            v3[a1[v4]] += v4
        v5, v6 = (collections.Counter(), collections.Counter())
        for v4 in reversed(range(len(a1))):
            v1[v4] += v6[a1[v4]] - v5[a1[v4]] * v4
            v5[a1[v4]] += 1
            v6[a1[v4]] += v4
        return v1
