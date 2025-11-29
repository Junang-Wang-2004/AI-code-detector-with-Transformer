class C1(object):

    def minNonZeroProduct(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = (pow(2, a1, v1) - 1) % v1
        v3 = (v2 - 1) % v1
        v4 = (pow(2, a1 - 1, v1 - 1) - 1) % (v1 - 1)
        return v2 * pow(v3, v4, v1) % v1
