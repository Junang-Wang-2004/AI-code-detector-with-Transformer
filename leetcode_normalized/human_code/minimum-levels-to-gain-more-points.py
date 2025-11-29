class C1(object):

    def minimumLevels(self, a1):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2 in range(len(a1)):
            v1[v2 + 1] = v1[v2] + (+1 if a1[v2] else -1)
        return next((v2 + 1 for v2 in range(len(a1) - 1) if v1[v2 + 1] > v1[-1] - v1[v2 + 1]), -1)
