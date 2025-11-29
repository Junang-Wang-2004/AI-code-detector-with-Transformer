class C1(object):

    def sumZero(self, a1):
        """
        """
        return [i for v1 in range(-(a1 // 2), a1 // 2 + 1) if not (v1 == 0 and a1 % 2 == 0)]
