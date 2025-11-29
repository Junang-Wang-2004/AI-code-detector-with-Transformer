class C1(object):

    def bestClosingTime(self, a1):
        """
        """
        v1 = v2 = v3 = 0
        for v4, v5 in enumerate(a1):
            v3 += 1 if v5 == 'Y' else -1
            if v3 > v2:
                v2 = v3
                v1 = v4 + 1
        return v1
