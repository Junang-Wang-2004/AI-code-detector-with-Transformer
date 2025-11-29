class C1(object):

    def sortByAbsoluteValue(self, a1):
        """
        """
        v1 = max((abs(x) for v2 in a1))
        v3 = [[] for v4 in range(v1 + 1)]
        for v2 in a1:
            v3[abs(v2)].append(v2)
        v5 = []
        for v2 in v3:
            v5.extend(v2)
        return v5
