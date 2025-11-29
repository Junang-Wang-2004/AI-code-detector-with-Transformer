class C1(object):

    def maximumScore(self, a1, a2):
        """
        """
        v1 = [0] * (len(a2) + 1)
        for v2, v3 in enumerate(reversed(a2), start=len(a1) - len(a2)):
            v1 = [max(v3 * a1[i] + v1[i + 1], v3 * a1[i + v2] + v1[i]) for v4 in range(len(v1) - 1)]
        return v1[0]
