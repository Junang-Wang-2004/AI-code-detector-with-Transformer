class C1(object):

    def maxTotalReward(self, a1):
        """
        """
        v1 = [False] * (max(a1) * 2 - 1 + 1)
        v1[0] = True
        for v2 in sorted(set(a1)):
            for v3 in range(v2):
                v1[v3 + v2] |= v1[v3]
        return next((v3 for v3 in reversed(range(len(v1))) if v1[v3]))
