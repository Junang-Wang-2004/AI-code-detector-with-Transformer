class C1(object):

    def evenProduct(self, a1):
        """
        """
        v1 = (len(a1) + 1) * len(a1) // 2
        v2 = 0
        for v3 in a1:
            v2 = v2 + 1 if v3 % 2 else 0
            v1 -= v2
        return v1
