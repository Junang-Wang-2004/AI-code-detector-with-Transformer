class C1(object):

    def lastVisitedIntegers(self, a1):
        """
        """
        v1 = 'prev'
        v2, v3 = ([], [])
        v4 = -1
        for v5 in a1:
            if v5 == v1:
                v2.append(v3[v4] if v4 >= 0 else -1)
                v4 -= 1
                continue
            v3.append(int(v5))
            v4 = len(v3) - 1
        return v2
