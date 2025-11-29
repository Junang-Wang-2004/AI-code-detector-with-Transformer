class C1(object):

    def averageValue(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            if v3 % 6:
                continue
            v1 += v3
            v2 += 1
        return v1 // v2 if v2 else 0
