import collections
import itertools

class C1(object):

    def rearrangeBarcodes(self, a1):
        """
        """
        v1 = 2
        v2 = collections.Counter(a1)
        v3 = max(v2.values())
        v4 = [0] * len(a1)
        v5 = (len(a1) - 1) % v1
        for v6 in itertools.chain((v6 for v6, v7 in v2.items() if v7 == v3), (v6 for v6, v7 in v2.items() if v7 != v3)):
            for v8 in range(v2[v6]):
                v4[v5] = v6
                v5 += v1
                if v5 >= len(v4):
                    v5 = (v5 - 1) % v1
        return v4
