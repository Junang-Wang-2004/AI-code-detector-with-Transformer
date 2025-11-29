class C1(object):

    def minimumDeletions(self, a1):
        """
        """
        v1, v2 = (a1.index(min(a1)), a1.index(max(a1)))
        if v1 > v2:
            v1, v2 = (v2, v1)
        return min(v1 + 1 + (len(a1) - v2), v2 + 1, len(a1) - v1)
