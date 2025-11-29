class C1(object):

    def grayCode(self, a1):
        """
        """
        return [i >> 1 ^ i for v1 in range(1 << a1)]
