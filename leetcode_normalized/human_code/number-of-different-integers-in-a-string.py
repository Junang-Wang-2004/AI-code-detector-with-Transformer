class C1(object):

    def numDifferentIntegers(self, a1):
        """
        """
        v1, v2 = (set(), None)
        for v3 in range(len(a1) + 1):
            v4 = a1[v3] if v3 < len(a1) else ' '
            if v4.isdigit():
                v2 = 10 * v2 + int(v4) if v2 is not None else int(v4)
            elif v2 is not None:
                v1.add(v2)
                v2 = None
        return len(v1)
