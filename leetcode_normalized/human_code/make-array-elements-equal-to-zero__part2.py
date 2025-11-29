class C1(object):

    def countValidSelections(self, a1):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2 in range(len(a1)):
            v1[v2 + 1] = v1[v2] + a1[v2]
        v3 = [0] * (len(a1) + 1)
        for v2 in reversed(range(len(a1))):
            v3[v2] = v3[v2 + 1] + a1[v2]
        return sum((max(2 - abs(v1[v2] - v3[v2 + 1]), 0) for v2 in range(len(a1)) if a1[v2] == 0))
