class C1(object):

    def reinitializePermutation(self, a1):
        """
        """
        v1, v2 = (0, 1)
        while not v1 or v2 != 1:
            v2 = v2 // 2 if not v2 % 2 else a1 // 2 + (v2 - 1) // 2
            v1 += 1
        return v1
