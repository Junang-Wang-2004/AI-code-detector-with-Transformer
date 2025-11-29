class C1(object):

    def secondHighest(self, a1):
        """
        """
        v1 = v2 = -1
        for v3 in a1:
            if not v3.isdigit():
                continue
            v4 = int(v3)
            if v4 > v1:
                v1, v2 = (v4, v1)
            elif v1 > v4 > v2:
                v2 = v4
        return v2
