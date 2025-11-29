import itertools

class C1(object):

    def widestPairOfIndices(self, a1, a2):
        """
        """
        v1 = {0: -1}
        v2 = v3 = 0
        for v4, (v5, v6) in enumerate(zip(a1, a2)):
            v3 += v5 - v6
            if v3 not in v1:
                v1[v3] = v4
            v2 = max(v2, v4 - v1[v3])
        return v2
