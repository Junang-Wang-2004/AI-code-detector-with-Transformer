class C1(object):

    def canCross(self, a1):
        """
        """
        if a1[1] != 1:
            return False
        v1 = {s: set() for v2 in a1}
        v1[1].add(1)
        for v2 in a1[:-1]:
            for v3 in v1[v2]:
                for v4 in (v3 - 1, v3, v3 + 1):
                    if v4 > 0 and v2 + v4 in v1:
                        v1[v2 + v4].add(v4)
        return bool(v1[a1[-1]])
