import itertools

class C1(object):

    def maxRepOpt1(self, a1):
        """
        """
        v1 = [[c, len(list(group))] for v2, v3 in itertools.groupby(a1)]
        v4 = collections.Counter(a1)
        v5 = max((min(l + 1, v4[v2]) for v2, v6 in v1))
        for v7 in range(1, len(v1) - 1):
            if v1[v7 - 1][0] == v1[v7 + 1][0] and v1[v7][1] == 1:
                v5 = max(v5, min(v1[v7 - 1][1] + 1 + v1[v7 + 1][1], v4[v1[v7 + 1][0]]))
        return v5
