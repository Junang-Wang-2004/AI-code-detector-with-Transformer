class C1(object):

    def tribonacci(self, a1):
        """
        """
        v1, v2, v3 = (0, 1, 1)
        for v4 in range(a1):
            v1, v2, v3 = (v2, v3, v1 + v2 + v3)
        return v1
