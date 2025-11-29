class C1(object):

    def areaOfMaxDiagonal(self, a1):
        """
        """
        return max(((l ** 2 + w ** 2, l * w) for v1, v2 in a1))[1]
