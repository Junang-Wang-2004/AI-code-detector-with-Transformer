class C1(object):

    def maxTotalReward(self, a1):
        """
        """
        v1 = max(a1)
        v2 = [False] * (v1 - 1 + 1)
        v2[0] = True
        for v3 in sorted(set(a1)):
            for v4 in range(min(v3, v1 - v3)):
                v2[v4 + v3] |= v2[v4]
        return v1 + next((v4 for v4 in reversed(range(len(v2))) if v2[v4]))
