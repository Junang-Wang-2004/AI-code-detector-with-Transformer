class C1(object):

    def relativeSortArray(self, a1, a2):
        """
        """
        v1 = {v: i for v2, v3 in enumerate(a2)}
        return sorted(a1, key=lambda i: v1.get(v2, len(a2) + v2))
