class C1(object):

    def smallestRepunitDivByK(self, a1):
        """
        """
        if a1 % 2 == 0 or a1 % 5 == 0:
            return -1
        v1 = 0
        for v2 in range(1, a1 + 1):
            v1 = (v1 * 10 + 1) % a1
            if not v1:
                return v2
        assert False
        return -1
