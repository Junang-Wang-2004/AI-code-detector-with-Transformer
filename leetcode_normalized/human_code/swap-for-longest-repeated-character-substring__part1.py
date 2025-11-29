import collections

class C1(object):

    def maxRepOpt1(self, a1):
        """
        """
        v1 = 1
        v2 = 0
        v3, v4 = (collections.Counter(), collections.Counter())
        v5, v6 = (0, 0)
        for v7 in range(len(a1)):
            v3[a1[v7]] += 1
            v4[a1[v7]] += 1
            v6 = max(v6, v4[a1[v7]])
            if v7 - v5 + 1 - v6 > v1:
                v4[a1[v5]] -= 1
                v5 += 1
            v2 = max(v2, min(v7 - v5 + 1, v3[a1[v7]]))
        return v2
