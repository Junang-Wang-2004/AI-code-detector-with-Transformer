class C1(object):

    def fairCandySwap(self, a1, a2):
        """
        """
        v1 = (sum(a1) - sum(a2)) // 2
        v2 = set(a1)
        for v3 in set(a2):
            if v1 + v3 in v2:
                return [v1 + v3, v3]
        return []
