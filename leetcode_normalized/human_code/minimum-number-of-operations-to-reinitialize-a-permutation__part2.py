class C1(object):

    def reinitializePermutation(self, a1):
        """
        """
        if a1 == 2:
            return 1
        v1, v2 = (0, 1)
        while not v1 or v2 != 1:
            v2 = v2 * 2 % (a1 - 1)
            v1 += 1
        return v1
