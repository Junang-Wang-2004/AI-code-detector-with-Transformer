class C1(object):

    def maximumLength(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in range(a2):
            v3 = [0] * a2
            for v4 in a1:
                v3[v4 % a2] = v3[(v2 - v4) % a2] + 1
            v1 = max(v1, max(v3))
        return v1
