import collections
import itertools

class C1(object):

    def calcEquation(self, a1, a2, a3):
        """
        """
        v1 = collections.defaultdict(dict)
        for (v2, v3), v4 in zip(a1, a2):
            v1[v2][v2] = v1[v3][v3] = 1.0
            v1[v2][v3] = v4
            v1[v3][v2] = 1.0 / v4
        for v4 in v1:
            for v5 in v1[v4]:
                for v6 in v1[v4]:
                    v1[v5][v6] = v1[v5][v4] * v1[v4][v6]
        return [v1[v2].get(v3, -1.0) for v2, v3 in a3]
