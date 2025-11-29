class C1(object):

    def circularPermutation(self, a1, a2):
        """
        """
        return [a2 ^ i >> 1 ^ i for v1 in range(1 << a1)]
