import collections

class C1(object):

    def rearrangeBarcodes(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        v2 = [[v, k] for v3, v4 in v1.items()]
        v2.sort(reverse=True)
        v5 = 0
        for v4, v3 in v2:
            for v6 in range(v4):
                a1[v5] = v3
                v5 += 2
                if v5 >= len(a1):
                    v5 = 1
        return a1
