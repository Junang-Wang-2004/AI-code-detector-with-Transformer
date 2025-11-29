class C1(object):

    def distinctDifferenceArray(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2 = set()
        for v3 in range(len(a1)):
            v2.add(a1[v3])
            v1[v3] = len(v2)
        v2.clear()
        for v3 in reversed(range(len(a1))):
            v1[v3] -= len(v2)
            v2.add(a1[v3])
        return v1
