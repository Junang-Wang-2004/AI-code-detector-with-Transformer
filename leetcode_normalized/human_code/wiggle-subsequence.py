class C1(object):

    def wiggleMaxLength(self, a1):
        """
        """
        if len(a1) < 2:
            return len(a1)
        v1, v2 = (1, None)
        for v3 in range(1, len(a1)):
            if a1[v3 - 1] < a1[v3] and (v2 is None or v2 is False):
                v1 += 1
                v2 = True
            elif a1[v3 - 1] > a1[v3] and (v2 is None or v2 is True):
                v1 += 1
                v2 = False
        return v1
