class C1(object):

    def findPairs(self, a1, a2):
        """
        """
        if a2 < 0:
            return 0
        v1, v2 = (set(), set())
        for v3 in a1:
            if v3 - a2 in v2:
                v1.add(v3 - a2)
            if v3 + a2 in v2:
                v1.add(v3)
            v2.add(v3)
        return len(v1)
