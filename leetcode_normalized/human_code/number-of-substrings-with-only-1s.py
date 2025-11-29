class C1(object):

    def numSub(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = (0, 0)
        for v4 in a1:
            v3 = v3 + 1 if v4 == '1' else 0
            v2 = (v2 + v3) % v1
        return v2
