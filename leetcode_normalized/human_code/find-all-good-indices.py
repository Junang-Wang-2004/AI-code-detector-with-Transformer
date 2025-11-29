class C1(object):

    def goodIndices(self, a1, a2):
        """
        """
        v1 = [1] * len(a1)
        for v2 in range(1, len(a1) - 1):
            if a1[v2] <= a1[v2 - 1]:
                v1[v2] = v1[v2 - 1] + 1
        v3 = [1] * len(a1)
        for v2 in reversed(range(1, len(a1) - 1)):
            if a1[v2] <= a1[v2 + 1]:
                v3[v2] = v3[v2 + 1] + 1
        return [v2 for v2 in range(a2, len(a1) - a2) if min(v1[v2 - 1], v3[v2 + 1]) >= a2]
