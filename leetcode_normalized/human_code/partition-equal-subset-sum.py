class C1(object):

    def canPartition(self, a1):
        """
        """
        v1 = sum(a1)
        if v1 % 2:
            return False
        v2 = [False] * (v1 / 2 + 1)
        v2[0] = True
        for v3 in a1:
            for v4 in reversed(range(1, len(v2))):
                if v3 <= v4:
                    v2[v4] = v2[v4] or v2[v4 - v3]
        return v2[-1]
