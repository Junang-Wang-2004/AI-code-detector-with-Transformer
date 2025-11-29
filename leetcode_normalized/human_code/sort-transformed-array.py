class C1(object):

    def sortTransformedArray(self, a1, a2, a3, a4):
        """
        """
        v1 = lambda x, a, b, c: a2 * x * x + a3 * x + a4
        v2 = []
        if not a1:
            return v2
        v3, v4 = (0, len(a1) - 1)
        v5 = -1 if a2 > 0 else 1
        while v3 <= v4:
            if v5 * v1(a1[v3], a2, a3, a4) < v5 * v1(a1[v4], a2, a3, a4):
                v2.append(v1(a1[v3], a2, a3, a4))
                v3 += 1
            else:
                v2.append(v1(a1[v4], a2, a3, a4))
                v4 -= 1
        return v2[::v5]
