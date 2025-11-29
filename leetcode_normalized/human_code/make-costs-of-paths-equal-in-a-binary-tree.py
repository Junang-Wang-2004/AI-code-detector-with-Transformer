class C1(object):

    def minIncrements(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in reversed(range(a1 // 2)):
            v1 += abs(a2[2 * v2 + 1] - a2[2 * v2 + 2])
            a2[v2] += max(a2[2 * v2 + 1], a2[2 * v2 + 2])
        return v1
