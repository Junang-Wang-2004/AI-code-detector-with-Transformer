class C1(object):

    def missingMultiple(self, a1, a2):
        """
        """
        v1 = set(a1)
        for v2 in range(1, len(v1) + 1):
            if v2 * a2 not in v1:
                return v2 * a2
        return (len(v1) + 1) * a2
