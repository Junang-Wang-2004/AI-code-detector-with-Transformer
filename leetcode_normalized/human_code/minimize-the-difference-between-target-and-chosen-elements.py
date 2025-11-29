class C1(object):

    def minimizeTheDifference(self, a1, a2):
        """
        """
        v1 = sum((min(row) for v2 in a1))
        if v1 >= a2:
            return v1 - a2
        v3 = {0}
        for v2 in a1:
            v3 = {total + x for v4 in v3 for v5 in v2 if v4 + v5 - a2 < a2 - v1}
        return min((abs(a2 - v4) for v4 in v3))
