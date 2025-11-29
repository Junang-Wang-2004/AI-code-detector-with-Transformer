class C1(object):

    def maxA(self, a1):
        """
        """
        if a1 < 7:
            return a1
        v1 = list(range(a1 + 1))
        for v2 in range(7, a1 + 1):
            v1[v2 % 6] = max(v1[(v2 - 4) % 6] * 3, v1[(v2 - 5) % 6] * 4)
        return v1[a1 % 6]
