class C1(object):

    def longestSquareStreak(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        a1.sort()
        v2 = -1
        for v3 in a1:
            v4 = int(v3 ** 0.5)
            if v4 ** 2 == v3:
                v1[v3] = v1[v4] + 1
            else:
                v1[v3] = 1
            v2 = max(v2, v1[v3])
        return v2 if v2 != 1 else -1
