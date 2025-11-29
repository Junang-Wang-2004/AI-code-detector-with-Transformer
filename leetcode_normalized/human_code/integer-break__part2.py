class C1(object):

    def integerBreak(self, a1):
        """
        """
        if a1 < 4:
            return a1 - 1
        v1 = [0, 1, 2, 3]
        for v2 in range(4, a1 + 1):
            v1[v2 % 4] = max(v1[(v2 - 2) % 4] * 2, v1[(v2 - 3) % 4] * 3)
        return v1[a1 % 4]
