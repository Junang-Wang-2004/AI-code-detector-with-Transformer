class C1(object):

    def minSum(self, a1, a2):
        """
        """
        v1 = sum((max(x, 1) for v2 in a1))
        v3 = sum((max(v2, 1) for v2 in a2))
        if v1 < v3:
            return v3 if 0 in a1 else -1
        if v1 > v3:
            return v1 if 0 in a2 else -1
        return v1
