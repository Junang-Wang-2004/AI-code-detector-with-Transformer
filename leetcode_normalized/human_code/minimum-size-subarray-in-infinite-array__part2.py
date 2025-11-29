class C1(object):

    def minSizeSubarray(self, a1, a2):
        """
        """
        v1 = float('inf')
        v2, a2 = divmod(a2, sum(a1))
        if not a2:
            return v2 * len(a1)
        v4 = v1
        v5 = {0: -1}
        v6 = 0
        for v7 in range(len(a1) - 1 + (len(a1) - 1)):
            v6 += a1[v7 % len(a1)]
            if v6 - a2 in v5:
                v4 = min(v4, v7 - v5[v6 - a2])
            v5[v6] = v7
        return v4 + v2 * len(a1) if v4 != v1 else -1
