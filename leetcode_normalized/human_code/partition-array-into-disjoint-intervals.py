class C1(object):

    def partitionDisjoint(self, a1):
        """
        """
        v1 = a1[:]
        for v2 in reversed(range(len(a1) - 1)):
            v1[v2] = min(v1[v2], v1[v2 + 1])
        v3 = 0
        for v2 in range(1, len(a1)):
            v3 = max(v3, a1[v2 - 1])
            if v3 <= v1[v2]:
                return v2
