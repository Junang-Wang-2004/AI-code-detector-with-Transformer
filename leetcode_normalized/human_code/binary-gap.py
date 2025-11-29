class C1(object):

    def binaryGap(self, a1):
        """
        """
        v1 = 0
        v2 = None
        for v3 in range(32):
            if a1 >> v3 & 1:
                if v2 is not None:
                    v1 = max(v1, v3 - v2)
                v2 = v3
        return v1
