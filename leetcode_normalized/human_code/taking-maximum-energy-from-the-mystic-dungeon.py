class C1(object):

    def maximumEnergy(self, a1, a2):
        """
        """
        v1 = float('-inf')
        for v2 in range(a2):
            v3 = 0
            for v4 in reversed(range((len(a1) - v2 - 1) % a2, len(a1) - v2, a2)):
                v3 += a1[v4]
                v1 = max(v1, v3)
        return v1
