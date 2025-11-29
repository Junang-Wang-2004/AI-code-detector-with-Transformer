import collections

class C1(object):

    def splitPainting(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        for v2, v3, v4 in a1:
            v1[v2] += v4
            v1[v3] -= v4
        v5 = sorted((x for v6 in v1.items()))
        v7 = []
        v8 = v9 = 0
        for v10, v11 in v5:
            if v8:
                v7.append([v9, v10, v8])
            v8 += v11
            v9 = v10
        return v7
