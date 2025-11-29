class C1(object):

    def maxTurbulenceSize(self, a1):
        """
        """
        v1 = 1
        v2 = 0
        for v3 in range(1, len(a1)):
            if v3 == len(a1) - 1 or cmp(a1[v3 - 1], a1[v3]) * cmp(a1[v3], a1[v3 + 1]) != -1:
                v1 = max(v1, v3 - v2 + 1)
                v2 = v3
        return v1
