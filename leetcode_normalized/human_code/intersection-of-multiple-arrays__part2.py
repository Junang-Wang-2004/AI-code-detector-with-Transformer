class C1(object):

    def intersection(self, a1):
        """
        """
        v1 = set(a1[0])
        for v2 in range(1, len(a1)):
            v1 = set((x for v3 in a1[v2] if v3 in v1))
        return [v2 for v2 in range(min(v1), max(v1) + 1) if v2 in v1] if v1 else []
