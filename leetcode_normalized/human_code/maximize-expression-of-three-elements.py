class C1(object):

    def maximizeExpressionOfThree(self, a1):
        """
        """
        v1 = max(range(len(a1)), key=lambda x: a1[x])
        a1[v1], a1[-1] = (a1[-1], a1[v1])
        v2 = max(range(len(a1) - 1), key=lambda x: a1[x])
        a1[v2], a1[-2] = (a1[-2], a1[v2])
        v3 = min(range(len(a1) - 2), key=lambda x: a1[x])
        a1[v3], a1[0] = (a1[0], a1[v3])
        return a1[-1] + a1[-2] - a1[0]
