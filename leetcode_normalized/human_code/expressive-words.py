import itertools

class C1(object):

    def expressiveWords(self, a1, a2):
        """
        """

        def RLE(a1):
            return zip(*[(k, len(list(grp))) for v1, v2 in itertools.groupby(a1)])
        v1, v2 = RLE(a1)
        v3 = 0
        for v4 in a2:
            v5, v6 = RLE(v4)
            if v5 != v1:
                continue
            v3 += all((c1 >= max(c2, 3) or c1 == c2 for v7, v8 in zip(v2, v6)))
        return v3
