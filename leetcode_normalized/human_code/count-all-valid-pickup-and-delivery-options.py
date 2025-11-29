class C1(object):

    def countOrders(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 1
        for v3 in reversed(range(2, 2 * a1 + 1, 2)):
            v2 = v2 * v3 * (v3 - 1) // 2 % v1
        return v2
