class C1(object):

    def triangularSum(self, a1):
        """
        """
        v1 = 0
        v2 = 1
        for v3 in range(len(a1)):
            v1 = (v1 + v2 * a1[v3]) % 10
            v2 *= len(a1) - 1 - v3
            v2 //= v3 + 1
        return v1
