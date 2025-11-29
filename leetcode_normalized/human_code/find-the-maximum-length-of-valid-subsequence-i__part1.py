class C1(object):

    def maximumLength(self, a1):
        """
        """
        v1 = 2
        v2 = 0
        for v3 in range(v1):
            v4 = [0] * v1
            for v5 in a1:
                v4[v5 % v1] = v4[(v3 - v5) % v1] + 1
            v2 = max(v2, max(v4))
        return v2
