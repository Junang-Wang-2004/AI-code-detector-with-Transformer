import collections
import fractions

class C1(object):

    def interchangeableRectangles(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        for v2, v3 in a1:
            v4 = fractions.gcd(v2, v3)
            v1[v2 // v4, v3 // v4] += 1
        return sum((c * (c - 1) // 2 for v5 in v1.values()))
