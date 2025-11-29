class C1(object):

    def subarrayBitwiseORs(self, a1):
        """
        """
        v1, v2 = (set(), {0})
        for v3 in a1:
            v2 = {v3} | {v3 | j for v4 in v2}
            v1 |= v2
        return len(v1)
