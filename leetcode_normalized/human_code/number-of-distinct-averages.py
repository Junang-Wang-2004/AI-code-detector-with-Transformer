class C1(object):

    def distinctAverages(self, a1):
        """
        """
        v1 = set()
        a1.sort()
        v2, v3 = (0, len(a1) - 1)
        while v2 < v3:
            v1.add(a1[v2] + a1[v3])
            v2, v3 = (v2 + 1, v3 - 1)
        return len(v1)
