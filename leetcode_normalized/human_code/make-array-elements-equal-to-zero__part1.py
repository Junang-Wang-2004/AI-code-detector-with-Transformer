class C1(object):

    def countValidSelections(self, a1):
        """
        """
        v1 = sum(a1)
        v2 = v3 = 0
        for v4 in a1:
            if not v4:
                v2 += max(2 - abs(v3 - (v1 - v3)), 0)
            else:
                v3 += v4
        return v2
