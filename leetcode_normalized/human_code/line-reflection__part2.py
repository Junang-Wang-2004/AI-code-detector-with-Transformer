class C1(object):

    def isReflected(self, a1):
        """
        """
        if not a1:
            return True
        a1.sort()
        a1[len(a1) / 2:] = sorted(a1[len(a1) / 2:], lambda x, y: y[1] - x[1] if x[0] == y[0] else x[0] - y[0])
        v1 = a1[0][0] + a1[-1][0]
        v2, v3 = (0, len(a1) - 1)
        while v2 <= v3:
            if v1 != a1[v2][0] + a1[v3][0] or (a1[v2][0] != a1[v3][0] and a1[v2][1] != a1[v3][1]):
                return False
            v2 += 1
            v3 -= 1
        return True
