import collections
from functools import reduce

class C1(object):

    def maximumProduct(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = collections.Counter(a1)
        v3 = min(v2.keys())
        while a2:
            v4 = min(v2[v3], a2)
            v2[v3] -= v4
            v2[v3 + 1] += v4
            if not v2[v3]:
                del v2[v3]
                v3 += 1
            a2 -= v4
        return reduce(lambda total, x: total * pow(x[0], x[1], v1) % v1, iter(v2.items()), 1)
