class C1(object):

    def evenProduct(self, a1):
        """
        """
        v1 = v2 = 0
        for v3, v4 in enumerate(a1):
            if v4 % 2 == 0:
                v2 = v3 + 1
            v1 += v2
        return v1
