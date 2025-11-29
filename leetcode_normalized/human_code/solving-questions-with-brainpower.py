class C1(object):

    def mostPoints(self, a1):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2 in reversed(range(len(v1) - 1)):
            v1[v2] = max(v1[v2 + 1], a1[v2][0] + (v1[v2 + 1 + a1[v2][1]] if v2 + 1 + a1[v2][1] < len(v1) else 0))
        return v1[0]
