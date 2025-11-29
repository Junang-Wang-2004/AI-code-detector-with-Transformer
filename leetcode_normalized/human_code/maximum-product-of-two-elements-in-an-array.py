class C1(object):

    def maxProduct(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            if v3 > v1:
                v1, v2 = (v3, v1)
            elif v3 > v2:
                v2 = v3
        return (v1 - 1) * (v2 - 1)
