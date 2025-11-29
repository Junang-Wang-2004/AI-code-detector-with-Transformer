class C1(object):

    def maxAbsValExpr(self, a1, a2):
        """
        """
        return max((max((c1 * a1[i] + c2 * a2[i] + i for v1 in range(len(a1)))) - min((c1 * a1[v1] + c2 * a2[v1] + v1 for v1 in range(len(a1)))) for v2 in [1, -1] for v3 in [1, -1]))
