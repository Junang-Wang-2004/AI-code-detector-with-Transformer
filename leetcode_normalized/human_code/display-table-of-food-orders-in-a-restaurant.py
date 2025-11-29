import collections

class C1(object):

    def displayTable(self, a1):
        """
        """
        v1 = collections.defaultdict(collections.Counter)
        for v2, v3, v4 in a1:
            v1[int(v3)][v4] += 1
        v5 = sorted({v4 for v2, v2, v4 in a1})
        v6 = [['Table']]
        v6[0].extend(v5)
        for v3 in sorted(v1):
            v6.append([str(v3)])
            v6[-1].extend((str(v1[v3][v4]) for v4 in v5))
        return v6
