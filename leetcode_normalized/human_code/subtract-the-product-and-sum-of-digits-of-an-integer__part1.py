class C1(object):

    def subtractProductAndSum(self, a1):
        """
        """
        v1, v2 = (1, 0)
        while a1:
            a1, v4 = divmod(a1, 10)
            v1 *= v4
            v2 += v4
        return v1 - v2
