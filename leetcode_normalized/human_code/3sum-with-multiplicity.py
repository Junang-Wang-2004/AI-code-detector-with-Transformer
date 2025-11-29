import collections
import itertools

class C1(object):

    def threeSumMulti(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1)
        v2 = 0
        for v3, v4 in itertools.combinations_with_replacement(v1, 2):
            v5 = a2 - v3 - v4
            if v3 == v4 == v5:
                v2 += v1[v3] * (v1[v3] - 1) * (v1[v3] - 2) // 6
            elif v3 == v4 != v5:
                v2 += v1[v3] * (v1[v3] - 1) // 2 * v1[v5]
            elif max(v3, v4) < v5:
                v2 += v1[v3] * v1[v4] * v1[v5]
        return v2 % (10 ** 9 + 7)
