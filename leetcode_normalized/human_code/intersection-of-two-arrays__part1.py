class C1(object):

    def intersection(self, a1, a2):
        """
        """
        if len(a1) > len(a2):
            return self.intersection(a2, a1)
        v1 = set()
        for v2 in a1:
            v1.add(v2)
        v3 = []
        for v2 in a2:
            if v2 in v1:
                v3 += (v2,)
                v1.discard(v2)
        return v3

    def intersection2(self, a1, a2):
        """
        """
        return list(set(a1) & set(a2))
