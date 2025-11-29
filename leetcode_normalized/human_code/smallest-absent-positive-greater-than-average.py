class C1(object):

    def smallestAbsent(self, a1):
        """
        """
        v1 = sum(a1)
        v2 = set(a1)
        return next((x for v3 in range(max(v1 // len(a1) + 1, 1), max(max(a1) + 1, 1) + 1) if v3 not in v2 and v3 * len(a1) > v1))
